import re

information_for_persons = {}

def input_error(func):
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
def hello_func(*Any, **Any2):
    answer = f"How can I help you?"
    return answer


@input_error
def add_func(name, phone):
    if name and phone:
        information_for_persons.update({name: phone})  
        answer = f"Your new contact added: {name} {phone}"
    else:
        raise IndexError    
    return answer


@input_error
def change_phone_func(name, phone):
    get_name = information_for_persons.get(name)

    if not get_name:
        raise ValueError
    else:    
        information_for_persons.update({name: phone})
        answer = f"The phone number for {name} is changed on {phone}"

    return answer

@input_error
def phone_func(name, phone):
    get_phone = information_for_persons.get(name)
    if not get_phone:
        raise ValueError
    else:
        answer = f"The phone number for contact {name} is {get_phone}"
    return answer


@input_error
def show_all_func(*Any, **Any2):
    answer = []
    if information_for_persons:
        for keys, values in information_for_persons.items():
            answer.append("{} {}".format(keys, values))
    else:
        raise ValueError("Your contacts list is empty") 
    return answer


@input_error
def exit_func(*Any, **Any2):
    answer = "Good bye!"
    return answer  

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

def validation_name(param):
    if re.findall(r"\D", param):
        result = param
    else:
        raise IndexError  

    return result

def validation_phone(param):
    if re.findall(r"\d", param):
        result = param
    else:
        raise IndexError  
            
    return result    


def input_func(input_string):
    name = ""
    phone = ""
    input_words = input_string.strip().lower().split()
    if input_string == "good bye":
        input_command = "good bye"
    elif input_string == "show all":
        input_command = "show all"
    else:
        input_command = input_words[0] 
        try:
            name = validation_name(input_words[1])
            try:
                phone = validation_phone(input_words[2])
            except:
                phone = "" 
        except:
            name = ""        

    return input_command, name, phone


def main():
    while True:
        input_string = input("Input command, please: ")
        input_command, name, phone = input_func(input_string)
        if input_command in BOT_COMMANDS:
            get_command = BOT_COMMANDS[input_command]
            print(get_command(name, phone))
            if get_command() == "Good bye!":
                break 
            else:
                continue              
        else:
            raise ValueError("I don't know this command. Try again.") 
                    
    return           


if __name__ == '__main__':
    main()    