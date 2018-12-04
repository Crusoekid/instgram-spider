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

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    'cookie': ''
}
