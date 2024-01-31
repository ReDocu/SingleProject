import pandas as pd
import numpy as np

from datetime import datetime

import requests
from bs4 import BeautifulSoup

import warnings
warnings.filterwarnings(action='ignore')

def create_game_info(game_id):

    # 데이터 프레임 구성하기
    game_info_columns = [
        'AppID',
        'Name',
        'Developer',
        'Company',
        'price',
        'latest rating',
        'latest rating counter',
        'all rating',
        'all rating counter',
        'release date',
        'category',
        'DLC_Game']

    df = pd.DataFrame(columns=game_info_columns)

    # 게임 인덱스 구성하기

    print(game_id)
    url = 'https://store.steampowered.com/app/{}/'.format(game_id)
    res = requests.get(url)
    soup = BeautifulSoup(res.text)
    # soup.select() 안에 값을 넣어서 찾아주세요
    # 'AppID'
    rev_game_id = game_id
    # 'Name', 게임 이름
    rev_game_name = (soup.select('#appHubAppName')[0].text)
    # 'Developer', 개발자
    rev_game_dev = (soup.select('#game_highlights > div.rightcol > div > div.glance_ctn_responsive_left > div:nth-child(3) > div.summary.column > a')[0].text)
    # 'Company', 배급사
    company_el = soup.select('#game_highlights > div.rightcol > div > div.glance_ctn_responsive_left > div:nth-child(4) > div.summary.column > a')
    rev_game_company = []
    for company in company_el:
        rev_game_company.append(company.text)
    # # 'price', 현재가격
    try:
        rev_game_price = (soup.select('.game_area_purchase_game > div.game_purchase_action > div > div.game_purchase_price.price')[0].text.strip())
    except:
        try:
            #game_area_purchase_section_add_to_cart_281619 > div.game_purchase_action
            #game_area_purchase_section_add_to_cart_281619 > div.game_purchase_action > div > div.discount_block.game_purchase_discount > div.discount_prices > div.discount_original_price
            rev_game_price = (soup.select('.game_area_purchase_game > div.game_purchase_action > div > div.discount_block.game_purchase_discount > div.discount_prices > div.discount_original_price')[0].text.strip())
        except:
            rev_game_price = 0
    
    print('게임가격 : ',rev_game_price)
    # # 'latest rating', 최근 평가
    
    try:
        rev_game_late_rating = (soup.select('#review_histogram_rollup_section > div.user_reviews_summary_bar > div > span.game_review_summary.positive')[0].text)
    except:
        rev_game_late_rating = np.nan
    # # 'latest rating counter', 최근 평가 인원
    try:
        rev_game_late_rating_counter = (soup.select('#review_histogram_recent_section > div.user_reviews_summary_bar > div > span:nth-child(3)')[0].text)
    except:
        rev_game_late_rating_counter = 0
    # # 'all rating', 모든 평가
    try:
        rev_game_all_rating = (soup.select('#review_histogram_rollup_section > div.user_reviews_summary_bar > div > span.game_review_summary.positive')[0].text)
    except:
        rev_game_all_rating = np.nan
    # # 'all rating counter', 모든 평가 인원
    try:
        rev_game_all_rating_count = (soup.select('#review_histogram_rollup_section > div.user_reviews_summary_bar > div > span:nth-child(3)')[0].text)
    except:
        rev_game_all_rating_count = 0
    # # 'release date', 출시일
    rev_game_release_date = (soup.select('#game_highlights > div.rightcol > div > div.glance_ctn_responsive_left > div.release_date > div.date')[0].text)
    # 'DLC_Game', DLC게임인 경우 '#game_area_purchase > div.game_area_bubble.game_area_dlc_bubble' 이 영역이 생깁니다. 
    # 예) https://store.steampowered.com/app/378649/The_Witcher_3_Wild_Hunt__Hearts_of_Stone/?curator_clanid=6126332
    # 장르
    company_category = soup.select('#genresAndManufacturer > span > a')
    rev_game_category = []
    for category in company_category:
        rev_game_category.append(category.text)
    try: 
        try:
            dlc_ori_id = soup.select('#game_highlights > div.rightcol > div > div.glance_details > p > a')[0]['href']
            rev_game_dlc_root = (''.join(filter(lambda x: x.isdigit(), dlc_ori_id)))
        except:
            rev_game_dlc_root = np.nan
        
        rev_game_matacritic_score = np.nan
    except:
        #print('dlc 아님') # 임시로 넣음 
        rev_game_dlc_root = np.nan
        rev_game_matacritic_score = (soup.select('#game_area_metascore > div.score.high')[0].text.strip())
        pass
    new_list = [
        rev_game_id,rev_game_name,rev_game_dev,rev_game_company,rev_game_price,rev_game_late_rating,rev_game_late_rating_counter,rev_game_all_rating,rev_game_all_rating_count,rev_game_release_date,rev_game_category,rev_game_dlc_root
    ]
    df.reset_index()
    df.loc[len(df)] = new_list

    # 데이터 최종 전처리
    df['price'] = df['price'].str.replace(',','')
    df['price'] = df['price'].str.replace('₩','')


    # 하드코딩 예외처리
    try:    
        df['price'] = df['price'].str.replace(',','')
        df['price'] = df['price'].str.replace('₩','')

        df['price'].iloc[df[df['price'] == 'Free'].index] = 0
        df['price'].iloc[df[df['price'] == 'Free To Play'].index] = 0
        df['price'].iloc[df[df['price'] == 'for Buddy Pass Users Only'].index] = 0
    
        df['price'] = df['price'].fillna(0)
    except:
        df['price'] = 0

   

    try:
        df['latest rating counter'] = df['latest rating counter'].str.replace(',','')
        df['latest rating counter'] = df['latest rating counter'].str.extract('(\d+)')
    except:
        df['latest rating counter'] = 0
    
    try:
        df['all rating counter'] = df['all rating counter'].str.replace(',','')
        df['all rating counter'] = df['all rating counter'].str.extract('(\d+)')
    except:
        df['all rating counter'] = 0
    #df['price'] = df['price'].astype(int)
    #df['latest rating counter'] = df['latest rating counter'].astype(int)
    #df['all rating counter'] = df['all rating counter'].astype(int)

    return df


def create_price_data(game_id):

    print("작업중 : ", game_id)

    game_info_df = pd.read_csv(r'static_data\game_info.csv')
    game_info_df['AppID'].astype(int)

    try:
        origin_price = game_info_df[game_info_df['AppID'] == game_id]['price']
    except:
        print(game_id , ' Fail')
        return 
    
    # 파일 확장자 찾기
    try:
        url = 'game_data\{}.csv'.format(game_id)
        df = pd.read_csv(url)
    except:
        print('{}Not CSV File'.format(game_id))
        pass

    try:
        url = 'game_data\{}.xlsx'.format(game_id)
        df = pd.read_excel(url)
    except:
        print('{}Not xlsx File'.format(game_id))
        
        pass



    df['Sale Start'] = np.nan
    df['Sale End'] = np.nan

    df['Origin Price'] = np.nan

    try:
        df['Origin Price'] = df['Origin Price'].fillna(int(origin_price.values[0]))
    except:
        df['Origin Price'] = df['Origin Price'].fillna(0)

    check_columns = []

    check_price_limit = 3

    if len(df) > check_price_limit - 1:
        for i in range(check_price_limit):
            check_columns.append(df['Final price'].iloc[0])
    else:
        for i in range(len(df)):
            check_columns.append(df['Final price'].iloc[0])

    if len(df) > check_price_limit - 1:
        for i in range(check_price_limit,len(df)):
            check_columns.append(df['Final price'][i-3:i].max())

    df['Origin Price'] = check_columns

    df['Sale Rate'] = round(1 - (df['Final price']/df['Origin Price']),2)
    df['Sale Rate']
    #for item in df[df['Sale Rate'] < 0].index:
    #    df['Origin Price'].iloc[item] = df['Final price'].iloc[item]
    #    df['Sale Rate'].iloc[item] = 0

    df['Sale Start'] = df['DateTime']

    # + 0 세일이 없음
    # + 1 세일이 끝났음을 의미 
    index_data = df[df['Final price'] != df['Origin Price']].index

    if len(index_data) > 0:
        check_data_list = index_data if index_data[len(index_data) - 1] + 1 < (len(df) - 1) else index_data[:-1]
        df['Sale End'].iloc[check_data_list] = df['DateTime'].iloc[check_data_list + 1]

        df = df.dropna()
        df = df.reset_index()

        df.drop(columns=['index'],inplace=True)

        df['Sale Start'] = pd.to_datetime(df['Sale Start'])
        df['Sale End'] = pd.to_datetime(df['Sale End'])
    
        ready_to_sales = []
    
        for i in range(len(df) - 1):
            ready_to_sales.append(df['Sale Start'].iloc[i + 1] - df['Sale End'].iloc[i])
    
    
        ready_to_sales.append(pd.to_datetime(datetime.today()) - df['Sale Start'].iloc[-1])
    
        df['Ready to Sale'] = ready_to_sales
        df['Sale Period'] = (df['Sale End'] - df['Sale Start'])
    else:
        return df.dropna()
    
    return df


#############################################
#
#############################################

def create_price_data_sub(game_id):

    print("작업중 : ", game_id)

    game_info_df = pd.read_csv(r'static_data\game_info.csv')
    game_info_df['AppID'].astype(int)
    try:
        origin_price = game_info_df[game_info_df['AppID'] == game_id]['price']
    except:
        print(game_id , ' Fail')
        return 
    
    # 파일 확장자 찾기
    try:
        url = 'game_data\{}.csv'.format(game_id)
        df = pd.read_csv(url)
    except:
        pass

    try:
        url = 'game_data\{}.xlsx'.format(game_id)
        df = pd.read_excel(url)
    except:
        pass

    if df == None:
        return None

    df['Sale Start'] = np.nan
    df['Sale End'] = np.nan

    df['Origin Price'] = np.nan
    try:
        df['Origin Price'] = df['Origin Price'].fillna(int(origin_price.values[0]))
    except:
        df['Origin Price'] = df['Origin Price'].fillna(0)

    check_columns = [df['Final price'].iloc[0],df['Final price'].iloc[0],df['Final price'].iloc[0]]
    
    if len(df) > 2:
        for i in range(3,len(df)):
            check_columns.append(df['Final price'][i-3:i].max())
    else:
        for i in range(len(df)):
            check_columns.append(origin_price)

    print(check_columns, "/", len(df))

    df['Origin Price'] = check_columns

    df['Sale Rate'] = round(1 - (df['Final price']/df['Origin Price']),2)
    df['Sale Rate']
    #for item in df[df['Sale Rate'] < 0].index:
    #    df['Origin Price'].iloc[item] = df['Final price'].iloc[item]
    #    df['Sale Rate'].iloc[item] = 0

    df = df[['Sale Start','Sale End','Final price','Origin Price','Sale Rate','DateTime']]

    df['Sale Start'] = df['DateTime']

    # + 0 세일이 없음
    # + 1 세일이 끝났음을 의미 
    index_data = df[df['Final price'] != df['Origin Price']].index
    check_data_list = index_data if index_data[len(index_data) - 1] + 1 < (len(df) - 1) else index_data[:-1]
    df['Sale End'].iloc[check_data_list] = df['DateTime'].iloc[check_data_list + 1]

    df = df.dropna()
    df = df.reset_index()

    df.drop(columns=['index'],inplace=True)

    df['Sale Start'] = pd.to_datetime(df['Sale Start'])
    df['Sale End'] = pd.to_datetime(df['Sale End'])

    ready_to_sales = []

    for i in range(len(df) - 1):
        ready_to_sales.append(df['Sale Start'].iloc[i + 1] - df['Sale End'].iloc[i])


    ready_to_sales.append(pd.to_datetime(datetime.today()) - df['Sale Start'].iloc[-1])

    df['Ready to Sale'] = ready_to_sales
    df['Sale Period'] = (df['Sale End'] - df['Sale Start'])

    return df

