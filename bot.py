information_for_persons = {}


def input_error(func):
    """
    Декоратор для обробки помилок при виконанні команд бота
    """
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "This name is wrong"
        except ValueError:
            return "The name is not in contacts"
        except TypeError:
            return "I don't know this command" 
        except IndexError:
            return "Please, print name and phone"   

    return inner


@input_error
def hello_func():
    """
    Ввічливий бот, вміє вітатися
    """
    answer = f"How can I help you?"

    return answer


@input_error
def add_func(data):
    """
    Додає дані (ім'я та номер телефону) до списку контактів
    """
    name, phone = validation_data(data)
    if name and phone:
        information_for_persons.update({name: phone})  
        answer = f"Your new contact added: {name} {phone}"
    else:
        raise IndexError    

    return answer


@input_error
def change_phone_func(data):
    """
    Змінює номер телефону за ім'ям контакта
    """
    name, phone = validation_data(data)
    get_name = information_for_persons[name]
    information_for_persons.update({name: phone})
    answer = f"The phone number for {name} is changed on {phone}"

    return answer


@input_error
def phone_func(name):
    """
    Повертає номер телефону за ім'ям контакта
    """
    new_name = name.strip()
    get_phone = information_for_persons.get(new_name)
    if not get_phone:
        raise ValueError
    else:
        answer = f"The phone number for contact {new_name}: {get_phone}"
    
    return answer


@input_error
def show_all_func():
    """
    Виводить на екран весь список контантів
    """
    contacts = ""
    if information_for_persons:
        for key, value in information_for_persons.items():
            contacts += f"{key}: {value}\n"
    else:
        raise ValueError("Your contacts list is empty") 
   
    return contacts


@input_error
def exit_func():
    """
    Закінчення роботи бота
    """
    return "Good bye!"


BOT_COMMANDS = {
    "hello": hello_func,
    "add": add_func,
    "change": change_phone_func,
    "phone": phone_func,
    "show all": show_all_func,
    "good bye": exit_func,
    "close": exit_func,
    "exit": exit_func
    }   


def bot_answer_func(question):
    """
    Функція повертає відповідь бота
    """
    return BOT_COMMANDS.get(question, incorrect_input_func)


def incorrect_input_func():
    """
    Функція корректної обробки невалідних команд для бота
    """
    return ValueError("I don't know this command. Try again.") 


def input_func(input_string):
    """
    Функція відокремлює слово-команду для бота
    """
    command = input_string
    data = ""
    for key in BOT_COMMANDS:
        if input_string.strip().lower().startswith(key):
            command = key
            data = input_string[len(command):]
            break
    if data:
        return bot_answer_func(command)(data)
    
    return bot_answer_func(command)()


def validation_data(data):
    """
    Функція перевіряє чи другим значенням введено ім'я, а третім номер телефону
    """
    new_data = data.strip().split(" ") 
    name = new_data[0]
    phone = new_data[1]
    if name.isnumeric():
        raise ValueError("Name must be in letters")
    if not phone.isnumeric():
        raise ValueError("Phone must be in numbers")   
    
    return name, phone


def main():
    """
    Користувач вводить команду для бота або команду, ім'я, номер телефону через пробіл
    Функція повертає відповідь бота
    Бот завершує роботу після слів "good bye" або "close" або "exit"
    """
    while True:
        input_string = input("Input command, please: ")
        get_command = input_func(input_string)
        print(get_command)
        if get_command == "Good bye!":
            break

    return           


if __name__ == '__main__':
    main()    