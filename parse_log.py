
status_logs =  [
                ['192.168.0.50', 'Ok'], ['192.168.0.51', 'Bad'], ['192.168.0.52', 'Ok'], ['192.168.0.53', 'Bad'],['192.168.0.54', 'Ok']
            ]
username_logs = [
                ['192.168.0.50', 'Vasya'], ['192.168.0.51', 'Vasya'], ['192.168.0.52', 'Petya'], ['192.168.0.53', 'Kolya'], ['192.168.0.54', 'Vasya']
            ],
status_reason = {'Bad': 'Porno', 'Ok': 'Work'}
final_logs=[]
ip_logs_ok= []
ip_logs_bad= []

for status in status_logs:
    for username_names in username_logs:
        for username in username_names:
            if username[0] == status[0]:
                final_logs.append("{} - {} - {} - {}".format(status[0], status[1], username[1], status_reason.get(status[1], 'unknown')))


print(final_logs)

