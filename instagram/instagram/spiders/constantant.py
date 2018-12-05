BASE_URL = 'https://www.instagram.com/'
BEGIN_URL = 'https://www.instagram.com/{0}/'

BASE_PHOTO_PATH = '../Photography/'
SAVE_PHOTO_PATH = '../Photography/{0}/'

SAVE_TEST_PATH = '../test/'
SAVE_PORTRAIT_PATH = '../portraits/'
SAVE_PIC_LINK = 'pic_Link.txt'

REQUEST_NEXT_PIC_URL = 'https://www.instagram.com/graphql/query/?query_hash=66eb9403e44cc12e5b5ecda48b667d41&variables=%7B%22id%22%3A%22{0}%22%2C%22first%22%3A12%2C%22after%22%3A%22{1}%22%7D' # userid,end_cursor

REQUEST_FOLLOWERS_URL = 'https://www.instagram.com/graphql/query/?query_hash=56066f031e6239f35a904ac20c9f37d9&variables=%7B%22id%22%3A%22{0}%22%2C%22include_reel%22%3Atrue%2C%22fetch_mutual%22%3Atrue%2C%22first%22%3A24%7D' # userid
REQUEST_NEXT_FOLLOWERS_URL = 'https://www.instagram.com/graphql/query/?query_hash=56066f031e6239f35a904ac20c9f37d9&variables=%7B%22id%22%3A%22{0}%22%2C%22include_reel%22%3Atrue%2C%22fetch_mutual%22%3Afalse%2C%22first%22%3A12%2C%22after%22%3A%22{1}%22%7D' # userid,end_cursor

REQUEST_SUGGEST_URL = 'https://www.instagram.com/graphql/query/?query_hash=ae21d996d1918b725a934c0ed7f59a74&variables=%7B%22fetch_suggested_count%22%3A10%2C%22include_media%22%3Afalse%7D'

COOKIE = 'mcd=3; mid=W_-VUQALAAHSuumxKG4Ti6zgH_4T; csrftoken=OsFGKtXF9kgXxjgDoyiSUk23jcGtQfrM; ds_user_id=9202495539; rur=FTW; sessionid=IGSC6982e378764690c26ec02935a535f9f300d49b785ed2c215bb3e029f0030a8f5%3An2620slGP0ufgx6YFiKLjyQ994IOOaSx%3A%7B%22_auth_user_id%22%3A9202495539%2C%22_auth_user_backend%22%3A%22accounts.backends.CaseInsensitiveModelBackend%22%2C%22_auth_user_hash%22%3A%22%22%2C%22_platform%22%3A4%2C%22_token_ver%22%3A2%2C%22_token%22%3A%229202495539%3AFUtfU7vx4Gz116APzCy1RxNKRVBn2n1z%3Ace7ef5a6a1895559558a4b8fde3115f07675c0c82fcdf5a85ee5593400b759d5%22%2C%22last_refreshed%22%3A1543567652.4002811909%7D; urlgen="{\"35.197.140.37\": 15169}:1gT0B8:6GmmD7M7lpLoG__KOjE6_ucKAzA"'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    'cookie': 'mcd=3; mid=W_-VUQALAAHSuumxKG4Ti6zgH_4T; csrftoken=OsFGKtXF9kgXxjgDoyiSUk23jcGtQfrM; ds_user_id=9202495539; rur=FTW; sessionid=IGSC6982e378764690c26ec02935a535f9f300d49b785ed2c215bb3e029f0030a8f5%3An2620slGP0ufgx6YFiKLjyQ994IOOaSx%3A%7B%22_auth_user_id%22%3A9202495539%2C%22_auth_user_backend%22%3A%22accounts.backends.CaseInsensitiveModelBackend%22%2C%22_auth_user_hash%22%3A%22%22%2C%22_platform%22%3A4%2C%22_token_ver%22%3A2%2C%22_token%22%3A%229202495539%3AFUtfU7vx4Gz116APzCy1RxNKRVBn2n1z%3Ace7ef5a6a1895559558a4b8fde3115f07675c0c82fcdf5a85ee5593400b759d5%22%2C%22last_refreshed%22%3A1543567652.4002811909%7D; urlgen="{\"35.197.140.37\": 15169}:1gT0B8:6GmmD7M7lpLoG__KOjE6_ucKAzA"'
}

G_SAVE_KIND = 'lz_instagram'
