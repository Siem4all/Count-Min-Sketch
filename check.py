import matplotlib.pyplot as plt

# Data for the graph
data = [
    {'mode': 'F2P', 'numCntrs': 4, 'Avg': 3.0250995153291332e-05, 'Lo': 2.9797476231181443e-05, 'Hi': 3.070451407540122e-05},
    {'mode': 'F2P', 'numCntrs': 24, 'Avg': 4.626098806084485e-06, 'Lo': 4.575022324489224e-06, 'Hi': 4.677175287679747e-06},
    {'mode': 'F2P', 'numCntrs': 44, 'Avg': 2.4182404048613017e-06, 'Lo': 2.3908402414998623e-06, 'Hi': 2.445640568222741e-06},
    {'mode': 'F2P', 'numCntrs': 64, 'Avg': 1.7212533150570092e-06, 'Lo': 1.7018190307666291e-06, 'Hi': 1.7406875993473893e-06},
    {'mode': 'F2P', 'numCntrs': 84, 'Avg': 1.1986331581809839e-06, 'Lo': 1.1837323722083874e-06, 'Hi': 1.2135339441535804e-06},
    {'mode': 'CEDAR', 'numCntrs': 4, 'Avg': 3.00336295150209e-05, 'Lo': 2.9403944947669662e-05, 'Hi': 3.066331408237214e-05},
    {'mode': 'CEDAR', 'numCntrs': 24, 'Avg': 4.6257231380937525e-06, 'Lo': 4.579557888174512e-06, 'Hi': 4.6718883880129926e-06},
    {'mode': 'CEDAR', 'numCntrs': 44, 'Avg': 2.4256234902879637e-06, 'Lo': 2.4030730172777275e-06, 'Hi': 2.4481739632982e-06},
    {'mode': 'CEDAR', 'numCntrs': 64, 'Avg': 1.734366630468119e-06, 'Lo': 1.7162171591083896e-06, 'Hi': 1.7525161018278485e-06},
    {'mode': 'CEDAR', 'numCntrs': 84, 'Avg': 1.2010773764404168e-06, 'Lo': 1.1899046879109282e-06, 'Hi': 1.2122500649699054e-06},
    {'mode': 'Morris', 'numCntrs': 4, 'Avg': 3.037717056706799e-05, 'Lo': 2.977899412459242e-05, 'Hi': 3.0975347009543564e-05},
    {'mode': 'Morris', 'numCntrs': 24, 'Avg': 4.63995465130162e-06, 'Lo': 4.593063843080023e-06, 'Hi': 4.686845459523218e-06},
    {'mode': 'Morris', 'numCntrs': 44, 'Avg': 2.4508878202598506e-06, 'Lo': 2.428452361188908e-06, 'Hi': 2.4733232793307934e-06},
    {'mode': 'Morris', 'numCntrs': 64, 'Avg': 1.7428743355395179e-06, 'Lo': 1.7221392906436063e-06, 'Hi': 1.7636093804354294e-06},
    {'mode': 'Morris', 'numCntrs': 84, 'Avg': 1.203733859492622e-06, 'Lo': 1.1905240728543947e-06, 'Hi': 1.2169436461308493e-06},
    {'mode': 'realCounter', 'numCntrs': 4, 'Avg': 3.195842898806624e-05, 'Lo': 3.195063620369702e-05, 'Hi': 3.1966221772435463e-05},
    {'mode': 'realCounter', 'numCntrs': 24, 'Avg': 4.754108660508754e-06, 'Lo': 4.752698654243569e-06, 'Hi': 4.7555186667739384e-06},
    {'mode': 'realCounter', 'numCntrs': 44, 'Avg': 2.4685495461034732e-06, 'Lo': 2.4677100567063058e-06, 'Hi': 2.4693890355006407e-06},
    {'mode': 'realCounter', 'numCntrs': 64, 'Avg': 1.764387829973833e-06, 'Lo': 1.7636165821300835e-06, 'Hi': 1.7651590778175824e-06},
    {'mode': 'realCounter', 'numCntrs': 84, 'Avg': 1.2467990642585363e-06, 'Lo': 1.2462217334055462e-06, 'Hi': 1.2473763951115264e-06}
]

# Create a color map for each mode
# Create a new figure
plt.figure()

# Iterate over each mode
for mode in set([d['mode'] for d in data]):
    # Get the data for the current mode
    mode_data = [d for d in data if d['mode'] == mode]

    # Extract the x and y values
    x = [d['numCntrs'] for d in mode_data]
    y = [d['Avg'] for d in mode_data]

    # Convert y values to e-02
    y = [val * pow(10, -2) for val in y]

    # Plot the data
    plt.plot(x, y, label=mode)

# Add a legend and axis labels
plt.legend()
plt.xlabel('Number of Counters')
plt.ylabel('Average (x10^-2)')

# Display the plot
plt.show()
