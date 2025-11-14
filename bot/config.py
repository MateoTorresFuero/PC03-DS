import os


class Config:
    def __init__(self):
        self.token = os.getenv("GITHUB_TOKEN")
        self.owner = os.getenv("GITHUB_OWNER", "pineda-404")
        self.repo = os.getenv("GITHUB_REPO", "PC03-DS")

        if not self.token:
            raise ValueError("GITHUB_TOKEN no está configurado")

    @property
    def repo_full_name(self):
        return f"{self.owner}/{self.repo}"
