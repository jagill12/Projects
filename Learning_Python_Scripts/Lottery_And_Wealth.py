import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

def GenerateLotteryNumbers():
    return random.sample(range(1, 43), 5)

def CountMatches(my_list, lottery_list):
    return sum(1 for x in my_list if x in lottery_list)

def PlayLottery():
    my_list = GenerateLotteryNumbers()
    lottery_list = GenerateLotteryNumbers()
    matches = CountMatches(my_list, lottery_list)
    if matches <= 1:
        return -1
    elif matches == 2:
        return 0
    elif matches == 3: 
        return 10
    elif matches == 4:
        return 197
    else:
        return 212534

def GetDisparityMessage(HighIncomeList, LowIncomeList, Decade):
    Wealthy = sum(HighIncomeList)
    Poor = sum(LowIncomeList)
    Wealthy_Percent = (Wealthy / (Wealthy + Poor)) * 100
    Poor_Percent = (Poor / (Wealthy + Poor)) * 100
    print(f"Decade {(Decade / 10)}: The high income group possesses {Wealthy_Percent:.2f}% of the community's wealth\n"
          f"while the low income group possesses {Poor_Percent:.2f}% of the community's wealth.")

def SimLottery(IncomeList, NumPlayers):
    player_indexes = random.sample(range(len(IncomeList)), NumPlayers)
    for idx in player_indexes:
        IncomeList[idx] += PlayLottery()
    return IncomeList

def AwardScholarship(IncomeList, AwardTotal):
    AwardTotalInt = int(AwardTotal)
    remainder = AwardTotal - AwardTotalInt

    for _ in range(AwardTotalInt):
        IncomeList[random.randrange(0, len(IncomeList))] += 1

    if remainder > 0:
        IncomeList[random.randrange(0, len(IncomeList))] += remainder

def SimCommunity(years, CommunitySize):
    HighIncomeList = [100] * (CommunitySize // 2)
    LowIncomeList = [99] * (CommunitySize // 2)

    HighIncomeRecord = [HighIncomeList.copy()]
    LowIncomeRecord = [LowIncomeList.copy()]

    for i in range(years):
        HighIncomeListCopy = HighIncomeRecord[-1].copy()
        LowIncomeListCopy = LowIncomeRecord[-1].copy()

        high_players = int(0.4 * len(HighIncomeListCopy))
        low_players = int(0.6 * len(LowIncomeListCopy))

        HighIncomeListCopy = SimLottery(HighIncomeListCopy, high_players)
        print(f"The High Income Record for year {i + 1} is {HighIncomeListCopy}")

        LowIncomeListCopy = SimLottery(LowIncomeListCopy, low_players)
        print(f"The Low Income Record for year {i + 1} is {LowIncomeListCopy}")

        TotalScholarships = 15
        HighIncomeScholarships = 0.7 * TotalScholarships
        LowIncomeScholarships = 0.3 * TotalScholarships

        AwardScholarship(HighIncomeListCopy, HighIncomeScholarships)
        HighIncomeRecord.append(HighIncomeListCopy)

        AwardScholarship(LowIncomeListCopy, LowIncomeScholarships)
        LowIncomeRecord.append(LowIncomeListCopy)

        if (i + 1) % 10 == 0:
            GetDisparityMessage(HighIncomeRecord[-1], LowIncomeRecord[-1], i + 1)

    plotSim(HighIncomeRecord, LowIncomeRecord)

def plotSim(highIncomeRecord, lowIncomeRecord):
    x = np.arange(len(highIncomeRecord))

    plotWealthRecord(x, highIncomeRecord, '#882255', '.')
    plotWealthRecord(x, lowIncomeRecord, '#44AA99', '*')

    plt.xlabel("Year")
    plt.ylabel("Wealth Value")
    magenta_patch = mpatches.Patch(color='#882255', label='High Income')
    teal_patch = mpatches.Patch(color='#44AA99', label='Low Income')
    plt.legend(handles=[magenta_patch, teal_patch])
    plt.show()

def plotWealthRecord(x, record, markerColor, markerShape):
    for i in range(len(record[0])):
        plotData = [record[j][i] for j in range(len(record))]
        plt.scatter(x, plotData, color=markerColor, marker=markerShape)

def simManyPlays(n):
    winnings = []
    reward = 0
    for i in range(n):
        reward += PlayLottery()
        winnings.append(reward)
    plt.xlabel("Number of Lottery Plays")
    plt.ylabel("Winnings")
    plt.plot(winnings, label="Total Winnings Over Time")
    plt.legend()
    plt.show()

def main():
    simManyPlays(1000)
    SimCommunity(80, 30)

main()
