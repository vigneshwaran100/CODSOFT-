todo_list=[]

while True:
    user_action= input("Enter Your Option ADD,REMOVE,REPLACE,SHOW,COMPLETE and EXIT: ")

    match user_action:
        case 'add' | 'ADD':
            todo_add=input("Enter Your Todo Task: ")
            todo_list.append(todo_add)

        case 'remove'| 'REMOVE':
            todo_remove=int(input("Enter Your Option To Remove Task: "))
            remove=todo_list[todo_remove-1]
            todo_list.remove(remove)
         
        case 'show' | 'SHOW':
            for index,i in enumerate(todo_list,1):
                  print(index,i)

        case 'replace' | 'REPLACE':
            word_index=int(input("Enter your word replace number: "))
            word_index=word_index-1
            new_word=input("Enter Your Replace Word: ")
            todo_list[word_index]=new_word
        
        case 'complete' | 'COMPLETE':
            todo_remove=int(input("Enter Your Option To completed Task: "))
            remove=todo_list[todo_remove-1]
            todo_list.remove(remove)

        case 'exit' | 'EXIT':
            break
print("Quit")
