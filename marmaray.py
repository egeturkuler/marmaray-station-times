import datetime

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

# Define the list of departure times for the "Last Train"
last_train_departures = [
    '22:50', '22:52', '22:54', '22:56', '22:58', '23:02', '23:05', '23:07',
    '23:09', '23:11', '23:13', '23:16', '23:19', '23:22', '23:24', '23:26',
    '23:28', '23:31', '23:33', '23:35', '23:37', '23:40', '23:42', '23:45',
    '23:47', '23:49', '23:52', '23:55', '23:59', '00:03', '00:06', '00:10',
    '00:12', '00:15', '00:17', '00:19', '00:22', '00:24', '00:27', '00:29',
    '00:32', '00:35'
]

# Calculate the time difference between each consecutive stop
time_differences = []
for i in range(len(stops) - 2):
    departure_time = datetime.datetime.strptime(last_train_departures[i], '%H:%M')
    arrival_time = datetime.datetime.strptime(last_train_departures[i + 1], '%H:%M')
    
    # Add 24 hours to the arrival time if it's before the departure time
    if arrival_time < departure_time:
        arrival_time += datetime.timedelta(days=1)
    
    time_diff = arrival_time - departure_time
    time_differences.append(time_diff)

# Handle the last stop separately
last_stop_index = len(stops) - 1
departure_time = datetime.datetime.strptime(last_train_departures[last_stop_index - 1], '%H:%M')
arrival_time = datetime.datetime.strptime('00:45', '%H:%M')
time_diff = arrival_time - departure_time
time_differences.append(time_diff)

# Print the results
for i in range(len(stops) - 1):
    print(f"Time between {stops[i]} and {stops[i + 1]}: {time_differences[i]}")

atakoy_index = stops.index('Ataköy')
print(atakoy_index)