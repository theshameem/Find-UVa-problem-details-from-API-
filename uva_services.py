import requests, json
import time
from requests import api

def get_json(url):
    hdr = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}
    response = requests.get(url, headers=hdr)
    return response.json()

#######################################UVA PROBLEM DETAILS#################################################
def uva_problem_details(id):
    api_url = "https://uhunt.onlinejudge.org/api/p/num/" + str(id).strip()
    json_data = get_json(api_url)

    uva_data = {
        'problem_id': json_data['pid'],
        'problem_title': json_data['title'],
        'time_limit': str(json_data['rtl']) + str(" ms").strip(),
        'problem_link': "https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=24&page=show_problem&problem=" + str(json_data['pid']).strip()
    }
    return uva_data


######################################MAIN FUNCTION CALL###################################################
if __name__ == '__main__':
    temp = [103, 108, 111, 116, 147]
    problem_number = [103, 108, 111, 116, 147, 164, 166, 182, 231, 242, 250, 323, 357, 431, 437, 473, 481, 495, 497, 507, 526, 531, 559, 562, 580, 585, 590, 607, 647, 662, 672, 674, 682, 702, 709, 714, 751, 757, 825, 828, 836, 861, 882, 899, 900, 907, 909, 910, 926, 950, 957, 959, 963, 970, 976, 983, 986, 988, 990, 991, 10003, 10029, 10032, 10050, 10051, 10066, 10069, 10072, 10074, 10081, 10086, 10091, 10097, 10100, 10118, 10128, 10130, 10131, 10149, 10154, 10157, 10163, 10192, 10198, 10201, 10207, 10239, 10243, 10247, 10254, 10261, 10271, 10280, 10304, 10306, 10313, 10324, 10328, 10337, 10359, 10364, 10365, 10405, 10419, 10444, 10446, 10453, 10454, 10465, 10487, 10497, 10502, 10516, 10518, 10529, 10532, 10534, 10536, 10541, 10559, 10564, 10568, 10590, 10593, 10597, 10599, 10604, 10616, 10617, 10625, 10626, 10634, 10635, 10643, 10648, 10651, 10654, 10658, 10667, 10681, 10684, 10688, 10690, 10692, 10694, 10702, 10711, 10712, 10715, 10721, 10722, 10723, 10733, 10739, 10743, 10747, 10755, 10759, 10788, 10791, 10811, 10817, 10819, 10820, 10826, 10827, 10835, 10839, 10859, 10860, 10874, 10888, 10891, 10904, 10908, 10910, 10911, 10913, 10918, 10930, 10934, 10943, 10953, 10980, 11002, 11003, 11008, 11022, 11026, 11031, 11040, 11052, 11067, 11069, 11077, 11081, 11084, 11088, 11091, 11104, 11125, 11126, 11133, 11137, 11151, 11162, 11169, 11171, 11176, 11181, 11191, 11218, 11229, 11252, 11258, 11259, 11261, 11264, 11266, 11280, 11282, 11284, 11285, 11288, 11293, 11303, 11307, 11310, 11311, 11318, 11320, 11324, 11328, 11341, 11361, 11365, 11370, 11372, 11375, 11391, 11394, 11400, 11404, 11405, 11413, 11420, 11421, 11427, 11431, 11432, 11433, 11441, 11444, 11450, 11456, 11471, 11472, 11481, 11485, 11486, 11499, 11502, 11514, 11515, 11517, 11523, 11531, 11532, 11534, 11545, 11546, 11552, 11553, 11555, 11566, 11569, 11578, 11584, 11590, 11598, 11601, 11605, 11611, 11617, 11645, 11653, 11691, 11753, 11790, 11908]

    mx = 0
    mn = 100000
    total = 0

    start = time.time()
    for num in problem_number:
        each_start_time = time.time()
        get_details = uva_problem_details(str(num))
        each_end_time = time.time()

        each_problem_time = each_end_time - each_start_time
        mx = max(mx, each_problem_time)
        mn = min(mn, each_problem_time)
        total = total + 1
        if total > 100:
            break
    end = time.time()
    avg = (end - start) / 100

    print(f"Max Time: {mx}\nMin Time: {mn}\nAverage Time: {avg}")

        
