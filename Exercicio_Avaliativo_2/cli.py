from teacher_crud import TeacherCRUD


class CLI:
    def __init__(self, teacher_crud):
        self.teacher_crud = teacher_crud

    def run(self):
        while True:
            print("1. Create Teacher")
            print("2. Read Teacher")
            print("3. Update Teacher")
            print("4. Delete Teacher")
            print("5. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                name = input("Enter Teacher's name: ")
                ano_nasc = int(input("Enter Teacher's year of birth: "))
                cpf = input("Enter Teacher's CPF: ")
                self.teacher_crud.create(name, ano_nasc, cpf)

            elif choice == '2':
                name = input("Enter Teacher's name: ")
                result = self.teacher_crud.read(name)
                print(result)

            elif choice == '3':
                name = input("Enter Teacher's name: ")
                new_cpf = input("Enter new CPF: ")
                result = self.teacher_crud.update(name, new_cpf)
                print(result)

            elif choice == '4':
                name = input("Enter Teacher's name: ")
                self.teacher_crud.delete(name)

            elif choice == '5':
                break

            else:
                print("Invalid choice. Please try again.")
