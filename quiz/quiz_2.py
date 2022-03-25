def exercise_1():
    import numpy as np
    won_array = []
    revenue_in_yen = [
        300000, 340000, 320000, 360000,
        440000, 140000, 180000, 340000,
        330000, 290000, 280000, 380000,
        170000, 140000, 230000, 390000,
        400000, 350000, 380000, 150000,
        110000, 240000, 380000, 380000,
        340000, 420000, 150000, 130000,
        360000, 320000, 250000
    ]
    # 코드를 작성하세요.
    
    # 정답 출력
    print(won_array)


def exercise_2():
    import numpy as np
    won_array = []
    revenue_in_yen = [
        300000, 340000, 320000, 360000,
        440000, 140000, 180000, 340000,
        330000, 290000, 280000, 380000,
        170000, 140000, 230000, 390000,
        400000, 350000, 380000, 150000,
        110000, 240000, 380000, 380000,
        340000, 420000, 150000, 130000,
        360000, 320000, 250000
    ]
    revenue_in_dollar = [
        1200, 1600, 1400, 1300,
        2100, 1400, 1500, 2100,
        1500, 1500, 2300, 2100,
        2800, 2600, 1700, 1400,
        2100, 2300, 1600, 1800,
        2200, 2400, 2100, 2800,
        1900, 2100, 1800, 2200,
        2100, 1600, 1800
    ]
    
    # 코드를 작성하세요.
    
    # 정답 출력
    print(won_array)


def exercise_3():
    import numpy as np
    bad_days_revenue = None
    # 코드를 작성하세요.
    
    # 정답 출력
    print(bad_days_revenue)


def exercise_4():
    import pandas as pd
    df = None
    # 코드를 작성하세요.
    
    # 정답 출력
    print(df)


def exercise_5():
    import pandas as pd
    
    df = pd.read_csv('data/silicon_valley_summary.csv')
    
    # 코드를 작성하세요.


def exercise_6():
    import pandas as pd
    # 원하는 경로에 csv 파일 저장 후 해당 파일을 불러오세요
    df = pd.read_csv('data/broadcast.csv', index_col=0)
    # 코드를 작성하세요.


def exercise_7():
    import pandas as pd
    
    df = pd.read_csv('data/silicon_valley_details.csv')
    
    # 코드를 작성하세요.


def exercise_8():
    import pandas as pd
    
    df = pd.read_csv('data/body_imperial2.csv', index_col=0)
    
    # 코드를 작성하세요.
    
    # 정답 출력
    print(df)


def exercise_9():
    import pandas as pd
    
    df = pd.read_csv('data/toeic.csv')
    
    # 코드를 작성하세요.
    
    # 정답 출력
    print(df)


def exercise_10():
    import pandas as pd
    
    df = pd.read_csv('data/gdp.csv', index_col=0)
    
    # 코드를 작성하세요.


if __name__ == '__main__':
    exercise_1()
    print('--------------------------------------------------------\n')
    exercise_2()
    print('--------------------------------------------------------\n')
    exercise_3()
    print('--------------------------------------------------------\n')
    exercise_4()
    print('--------------------------------------------------------\n')
    exercise_5()
    print('--------------------------------------------------------\n')
    exercise_6()
    print('--------------------------------------------------------\n')
    exercise_7()
    print('--------------------------------------------------------\n')
    exercise_8()
    print('--------------------------------------------------------\n')
    exercise_9()
    print('--------------------------------------------------------\n')
    exercise_10()
