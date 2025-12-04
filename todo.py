import json
from pathlib import Path
from datetime import datetime

class TodoManager:
    def __init__(self, path="tasks.json"):
        self.path = Path(path)
        self.tasks = []
        self._load()

    def _load(self):
        if self.path.exists():
            try:
                self.tasks = json.loads(self.path.read_text())
            except json.JSONDecodeError:
                print("Warning: tasks.json is corrupted, starting with empty list.")
                self.tasks = []
        else:
            self.tasks = []

    def _save(self):
        self.path.write_text(json.dumps(self.tasks, indent=2, ensure_ascii=False))

    def list_tasks(self):
        if not self.tasks:
            print("No tasks.")
            return
        for i, t in enumerate(self.tasks, 1):
            status = "done" if t.get("done") else " "
            urgent = "(!)" if t.get("urgent") else ""
            created = t.get("created", "")
            print(f"{i}. [{status}] {t['description']} {urgent} - created: {created}")

    def add_task(self, description, urgent=False):
        # TODO:
        # 1. Adicionar um novo parâmetro 'urgent=False' a esta função
        # 2. Guardar no dicionário da tarefa a chave 'urgent': urgent
        # 3. Atualizar chamadas em main.py para passar esse parâmetro
        task = {
            "description": description,
            "done": False,
            # 'urgent' não está presente - é aqui que os alunos devem adicionar
            "urgent": urgent,
            "created": datetime.utcnow().isoformat() + "Z"
        }
        self.tasks.append(task)
        self._save()
        print("Task added.")

    def mark_done(self, index):
        try:
            task = self.tasks[index - 1]
        except IndexError:
            print("Invalid task id.")
            return
        task["done"] = True
        self._save()
        print("Task marked as done.")

    def remove_task(self, index):
        try:
            self.tasks.pop(index - 1)
            self._save()
            print("Task removed.")
        except IndexError:
            print("Invalid task id.")
