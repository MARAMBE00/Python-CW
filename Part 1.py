# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: w1867457
# Date: 08/12/2021

total_credits = 0
progress_count = 0
trailer_count = 0
retriever_count = 0
excluded_count = 0

staff_version_loop = True

while staff_version_loop:
    while True:
        while True:
            try:
                pass_credits = int(input('Please enter your credits at pass: '))
                if 0<=pass_credits<=120 and pass_credits % 20 == 0:
                    break
                print('Out of range')
                print()
            except ValueError:
                print('Integer required')
                print()
                
        while True:
            try:    
                defer_credits = int(input('Please enter your credits at defer: '))
                if 0<=defer_credits<=120 and defer_credits % 20 == 0:
                    break
                print('Out of range')
                print()
            except ValueError:
                print('Integer required')
                print()
                   
        while True:
            try:  
                fail_credits = int(input('Please enter your credits at fail: '))
                if 0<=fail_credits<=120 and fail_credits % 20 == 0:
                    break
                print('Out of range')
                print()
            except ValueError:
                print('Integer required')
                print()

        total_credits = pass_credits + defer_credits + fail_credits
        if total_credits == 120:
            break
        print('Total incorrect')
        print()

    if pass_credits == 120:
        print('Progress')
        progress_count += 1
    elif pass_credits == 100:
        print('Progress (module trailer)')
        trailer_count += 1
    elif 80<=fail_credits<=120:
        print('Exclude')
        excluded_count += 1
    else:
        print('Do not progress – module retriever')
        retriever_count += 1

    print()

    while True:
        staff_version = input('Would you like to enter another set of data?\n'"Enter 'y' for yes or 'q' to quit and view results: ").lower()
        if staff_version == 'y':
            staff_version_loop = True
            break
        elif staff_version == 'q':
            staff_version_loop = False

            print()
            print('-----------------------------------------------------')
            print('\t''\t''Horizontal Histogram')
            print()
            print('Progress', progress_count, ' :', '*' * progress_count)
            print('Trailer', trailer_count, '  :', '*' * trailer_count)
            print('Retriever', retriever_count, ':', '*' * retriever_count)
            print('Excluded', excluded_count, ' :', '*' * excluded_count)

            print()
            print(progress_count+trailer_count+retriever_count+excluded_count, 'outcomes in total.')
            print('-----------------------------------------------------')
            break
    print()
