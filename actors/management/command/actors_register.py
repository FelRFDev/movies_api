from django.core.management.base import BaseCommand

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(
            'file_name',
            type=str,
            help='Name of the file with Actors data.'
        )
    
    def handle(self, *args, **options):
        file = options['file_name']
        file_name=options['file_name']
        with open(file=file_name, mode='r', encoding='utf-8') as file:
            data = csv.DictReader(file)
            for row in data:
                name = row['name']
                birthdate = datetime.strptime(row['birthdate'], '%Y-%m-%d').date()
                nationality = row['nationality']

                Actor.objects.create(
                    name = name,
                    birthdate = birthdate,
                    nationallity = nationality,
                )
                self.stdout.write(self.style.NOTICE(f'The actor [{name}] was successfuly registerd at the the database!'))
        self.stdout.write(self.style.SUCCESS('Database import finished successfully!'))
