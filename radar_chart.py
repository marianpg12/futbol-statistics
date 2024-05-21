#!/usr/bin/python3
import streamlit
import numpy
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def radar_chart(players=['V. van Dijk','M. Salah'], title="Virgil van Dijk Vs Mo Salah"):
    """
    INPUT: 
    players: Player names(1D-array)
    title : Title for the chart(str)
    
    OUTPUT 
    Plots Radar Chart
    """
    labels=np.array(['PAC','SHO', 'PAS', 'DRI','PHY','DEF'])
    angles=np.linspace(0, 2*np.pi, len(labels), endpoint=False)
    angles=np.concatenate((angles,[angles[0]]))

    fig=plt.figure(figsize=(6,6))
    plt.suptitle(title)
    for player in players:
        stats=np.array(df[df.Name==player][labels])[0]
        stats=np.concatenate((stats,[stats[0]]))

        ax = fig.add_subplot(111, polar=True)
        ax.plot(angles, stats, 'o-', linewidth=2, label=player)
        ax.fill(angles, stats, alpha=0.25)
        ax.set_thetagrids(angles * 180/np.pi, labels)

    ax.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()
    
radar_chart()
