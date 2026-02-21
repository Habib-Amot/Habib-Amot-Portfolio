from pathlib import Path
from django.conf import settings
import argparse
from django.core.management import BaseCommand
from django.core.management.base import CommandParser


class Command(BaseCommand):
    APPLICATION_FOLDER = Path(settings.BASE_DIR) / 'applications'

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument('name', type=str, help="the name of the API app to create inside applicaion")
        parser.add_argument('-aV', '--api-version', type=str, default='1', help="the version number of the api app")

    def handle(self, *args: argparse.Any, **options: argparse.Any) -> str | None:
        app_name = self.APPLICATION_FOLDER / Path(options.get('name'))

        app_folders = [
            'migrations',
            'services',
            'apis',

        ]
        app_files = [
            '__init__.py',
            'admin.py',
            'apps.py',
            'models.py',
            'serializers.py',
            'tests.py',
            'urls.py',
            'views.py'
        ]
        api_version_folder = 'v' + str(options.get('api_version'))

        app_name.mkdir(parents=True, exist_ok=True)

        for folder in app_folders:
            if folder.lower() == 'apis':
                Path(app_name / folder).mkdir(parents=True, exist_ok=True)
                Path.touch(app_name / folder / '__init__.py', exist_ok=True)
                version_path = app_name / folder / api_version_folder
                version_path.mkdir(parents=True, exist_ok=True)
                Path.touch(version_path / 'views.py', exist_ok=True)
                Path.touch(version_path / 'urlss.py', exist_ok=True)
            else:
                Path(app_name / folder).mkdir(exist_ok=True, parents=True)
        
        for file in app_files:
            Path.touch(app_name / file, exist_ok=True)