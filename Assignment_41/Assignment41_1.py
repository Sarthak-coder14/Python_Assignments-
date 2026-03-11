import math

def Euclidean_dist(P1,P2):
    distance = math.sqrt((P1['x'] - P2['x'])**2 + (P1['y'] - P2['y'])**2)
    return distance

def main():
    Border = "-"*50
    print("Enter X co-ordinate : ")
    X = int(input())

    print("Enter Y co-ordinate : ")
    Y = int(input())

    data = [
        {'point': 'A', 'x': 1, 'y': 2, 'label': 'Red'},
        {'point': 'B', 'x': 2, 'y': 3, 'label': 'Red'},
        {'point': 'C', 'x': 3, 'y': 1, 'label': 'Blue'},
        {'point': 'D', 'x': 6, 'y': 5, 'label': 'Blue'}
    ]
    print(Border)
    print("Training data set:")
    print(Border)
    for d in data:
        print(d)

    new_point = {'x': X, 'y': Y}
    print(Border)
    print("Calulate Euclidean distance of each point : ")
    print(Border)
    for d in data:
        d['distance'] = Euclidean_dist(d, new_point)
        print(d)
    
    print(Border)
    print("Sorting Distance by acending order : ")
    print(Border)
    sorted_data = sorted(data, key=lambda item: item['distance'])

    for i in range(len(sorted_data)):
        print(sorted_data[i])
    
    print(Border)
    print("First 3 distance : ")
    print(Border)
    K = 3
    k_nearest = sorted_data[:K]  
    for i in range(len(k_nearest)):
        print(k_nearest[i]) 

    red = sum(1 for i in k_nearest if i['label'] == 'Red')
    blue = sum(1 for i in k_nearest if i['label'] == 'Blue')   

    if red > blue:
        print("Predicted class = Red")
    else:
        print("Predicted class = Blue")

if __name__ == "__main__":
    main()