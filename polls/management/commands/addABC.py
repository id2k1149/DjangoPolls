from django.core.management.base import BaseCommand
from polls.models import Answer
import string
from random import randrange
from faker import Faker


class Command(BaseCommand):

    def handle(self, *args, **options):
        faker = Faker('en_us')
        alphabet_string = string.ascii_uppercase
        alphabet_list = list(alphabet_string)

        Answer.objects.all().delete()
        for each in alphabet_list:
            i = 1
            # print("new for ", each)
            new_name = faker.company()
            # new_name = 'Тест Компания ' + each
            print(new_name)
            Answer.objects.create(answer=new_name)
            company_id = int(Company.objects.get(name=new_name).id)
            # print(type(company_id), " company_id =", company_id)
            dep_name = each + '-' + str(i)

            head_name = faker.name()
            # print(head_name)

            Department.objects.create(department_name=dep_name,
                                      company_id=company_id,
                                      head_of_department=head_name)

            while i <= 2:
                r1 = randrange(3)
                j = 1
                # print("new while ", "each = ", each, "i = ", i, "j = ", j)
                dep_pk = Department.objects.get(department_name=dep_name).id
                while j <= r1:
                    dep_name_j = each + each + str(i) + '-' + str(j)
                    head_name = faker.name()
                    Department.objects.create(department_name=dep_name_j,
                                              company_id=company_id,
                                              parent_id=dep_pk,
                                              head_of_department=head_name)
                    print("dep created ", dep_name, dep_pk)
                    r2 = randrange(3)
                    k = 1
                    while k <= r2:
                        dep_pk = Department.objects.get(department_name=dep_name_j).id
                        dep_name_k = each + dep_name_j + '-' + str(k)
                        head_name = faker.name()
                        Department.objects.create(department_name=dep_name_k,
                                                  company_id=company_id,
                                                  parent_id=dep_pk,
                                                  head_of_department=head_name)
                        k += 1
                    j += 1
                i += 1

        print('end')
