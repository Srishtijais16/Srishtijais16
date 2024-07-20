do_list = []
done_count = 0

while True:
    print("1. Adding Task")
    print("2. Completion Task")
    print("3. Tracking the task")
    print("4. completed")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        to_do = input("Enter the task description: ")
        do_list.append(to_do)
        print(f"Task added: {to_do}")
    elif choice == 2:
        if do_list:
            for i, task in enumerate(do_list):
                print(f"{i}: {task}")
            task_number = int(input("Enter the task number to mark as complete: "))
            if 0 <= task_number < len(do_list):
                completed_task = do_list.pop(task_number)
                done_count += 1
                print(f"Task '{completed_task}' completed.")
            else:
                print("Invalid task number.")
        else:
            print("No tasks to complete.")
    elif choice == 3:
        if do_list or done_count:
            task_percent = (done_count / (done_count + len(do_list))) * 100
        else:
            task_percent = 0
        print(f"The completed task percentage is {task_percent:.2f}%.")
    elif choice == 4:
        print("completed")
        break
    else:
        print("Invalid choice.")