class SettingsService:
    """Simulates  API for settings"""

    def __init__(self, qt_app):
        self.qt_app = qt_app

    def get_settings(self) -> dict:
        return {"theme": "dark_blue.xml", "notifications_enabled": True}

    def apply_stylesheet(self, theme: str, invert_secondary: bool = False):
        from qt_material import apply_stylesheet

        apply_stylesheet(self.qt_app, theme, invert_secondary=invert_secondary)
