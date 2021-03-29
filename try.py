
try:
    f = open('logs/wrning.log')
except FileNotFoundError as e:
    print(e)
    print('Error in filename')
except Exception as e:
    print(e)
else:
    print(f.read())
    f.close()
finally:
    print('All done')