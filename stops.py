# Define the list of stops
stops = [
    'Gebze', 'Darıca', 'Osmangazi', 'Fatih', 'Çayırova', 'Tuzla', 'İçmeler',
    'Aydıntepe', 'Güzelyalı', 'Tersane', 'Kaynarca', 'Pendik', 'Yunus',
    'Kartal', 'Başak', 'Atalar', 'Cevizli', 'Maltepe', 'Süreyya Plajı',
    'İdealtepe', 'Küçükyalı', 'Bostancı', 'Suadiye', 'Erenköy', 'Göztepe',
    'Feneryolu', 'Söğütlü Ç', 'Ayrılık Ç', 'Üsküdar', 'Sirkeci', 'Yenikapı',
    'Kazlıçeşme', 'Zeytinburnu', 'Yenimahalle', 'Bakırköy', 'Ataköy', 'Yeşilyurt',
    'Yeşilköy', 'Akvaryum', 'Florya', 'Küçük çekmece', 'Mustafa Kemal', 'Halkalı'
]

# Define the list of departure times for different trains
first_train_departures = [
    ['06:05', '06:07', '06:09', '06:11', '06:13', '06:03', '06:06', '06:08', '06:10', '06:12', '06:14', '06:02', '06:05', '06:08', '06:10', '06:12', '06:14', '06:02', '06:04', '06:06', '06:08', '06:11', '06:13', '06:00', '06:02', '06:04', '06:00', '06:10', '05:59'],
    ['06:03', '06:06', '06:10', '06:12', '06:02', '06:04', '06:06', '06:09', '06:11', '06:14', '06:16', '06:19', '06:22'],
    ['06:20', '06:22', '06:24', '06:26', '06:28', '06:18', '06:21', '06:23', '06:25', '06:27', '06:29', '06:09', '06:12', '06:13', '06:15', '06:17', '06:19', '06:09', '06:11', '06:13', '06:12', '06:15', '06:12', '06:07', '06:10', '06:12', '06:07', '06:15', '06:07', '06:11', '06:15', '06:18', '06:20', '06:08', '06:10', '06:21', '06:24', '06:26', '06:29', '06:31', '06:34', '06:37'],
    ['22:50', '22:52', '22:54', '22:56', '22:58', '23:02', '23:05', '23:07', '23:09', '23:11', '23:13', '23:16', '23:19', '23:22', '23:24', '23:26', '23:28', '23:31', '23:33', '23:35', '23:37', '23:40', '23:42', '23:45', '23:47', '23:49', '23:52', '23:55', '23:59', '00:03', '00:06', '00:10', '00:12', '00:15', '00:17', '00:19', '00:22', '00:24', '00:27', '00:29', '00:32', '00:35']
]

# Define the list of departure times for the "Last Train"
last_train_departures = [
    '22:50', '22:52', '22:54', '22:56', '22:58', '23:02', '23:05', '23:07',
    '23:09', '23:11', '23:13', '23:16', '23:19', '23:22', '23:24', '23:26',
    '23:28', '23:31', '23:33', '23:35', '23:37', '23:40', '23:42', '23:45',
    '23:47', '23:49', '23:52', '23:55', '23:59', '00:03', '00:06', '00:10',
    '00:12', '00:15', '00:17', '00:19', '00:22', '00:24', '00:27', '00:29',
    '00:32', '00:35'
]

# Time between trains is 8 minutes between Ataköy and Pendik
# Time between trains is 15 minutes between Halkalı and Gebze

def get_arrival_times(station_index):
    arrival_times = []
    # Find the positions of Ataköy and Pendik
    atakoy_index = stops.index('Ataköy')
    pendik_index = stops.index('Pendik')
    for j, train_schedule in enumerate(first_train_departures):
        if station_index < len(train_schedule):
            current_time = train_schedule[station_index]
            last_time = last_train_departures[station_index]
            while current_time <= last_time:
                arrival_times.append(current_time)
                hour, minute = map(int, current_time.split(':'))
                # Check if the station is between Ataköy and Pendik
                if atakoy_index <= station_index <= pendik_index or pendik_index <= station_index <= atakoy_index:
                    minute += 8  # Time between trains is 8 minutes between Ataköy and Pendik
                else:
                    minute += 15  # Time between trains is 15 minutes between Halkalı and Gebze
                if minute >= 60:
                    hour += 1
                    minute -= 60
                current_time = f"{hour:02d}:{minute:02d}"
                # Break the loop if the current time exceeds the last scheduled departure time
                if current_time > last_time:
                    break
    return arrival_times

station_name = input("Enter the train station name: ")
if station_name in stops:
    station_index = stops.index(station_name)
    arrival_times = get_arrival_times(station_index)
    if arrival_times:
        print(f"Arrival times at {station_name}:")
        for time in arrival_times:
            print(time)
    else:
        print(f"No trains stop at {station_name}.")
else:
    print(f"There are no stops at {station_name}.")

