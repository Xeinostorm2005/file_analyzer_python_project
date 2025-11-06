from src.main import main

try:
    main()
except KeyboardInterrupt:
    print("Thank for using our analyzer!")
    exit()
except NameError as error:
    print('It seems that the devs messed up!!')
    print('Error: ',error)
    input('Press enter to exit...')
    exit()