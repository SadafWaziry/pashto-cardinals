# -*- coding: utf-8 -*-

one_to_nineteen_list = ['صفر', 'یو', 'دوه', 'درې', 'څلور', 'پنڂه', 'شپږ', 'اووه', 'اته', 'نهه', 'لس', 'یوولس', 'دولس', 'دیارلس', 'څوارلس', 'پنڂه لس', 'شپاړس', 'اوولس', 'اتلس', 'نولس' ]

ten_to_twenty_list = ['صفر', 'لس', 'ویشت', 'دېرش', 'څلوېښت', 'پنڂوس', 'شپېته', 'اویا', 'اتیا', 'نوي']

thousand_to_more_list = ['', 'زر', 'ملیون', 'ملیارد',]


def less_than_thousnds(number):
    num = int(number)
    if 0 <= num <= 19:
        return one_to_nineteen_list[num]
    elif 20 <= num <= 99:
        if num == 20:
            return " شل"
        elif number[-1] == "0":
            return ten_to_twenty_list[int(number[0])]
        else:
            return one_to_nineteen_list[int(number[1])]  + " " + ten_to_twenty_list[int(number[0])]
    elif 100 <= num <= 999:
        reminder = num % 100
        division = num / 100
        if reminder == 0:
            if num == 100:
                return " سل"
            else:
                return one_to_nineteen_list[division] + " سوه"
        elif 101 <= num <= 199:
            return one_to_nineteen_list[division] + " سل او " + less_than_thousnds(str(reminder))
        else:
            return one_to_nineteen_list[division] + " سوه او  " + less_than_thousnds(str(reminder))


def greater_than_thousand(number):
    num = int(number)
    get_thousands_array = get_thousands(num)
    array_len = len(get_thousands_array) - 1
    new_array = []
    for z in get_thousands_array[::-1]:
        thousands = less_than_thousnds(str(z)) + " "
        up_thousands = thousand_to_more_list[array_len] + ", "
        if thousands == " ":
            break
        elif thousands == "صفر ":
            thousands, up_thousands = "", ""
        new_array.append(thousands + up_thousands)
        array_len -= 1
    num_to_words = "".join(new_array).strip()
    if num_to_words[-1] == ",":
        num_to_words = num_to_words[:-1]
    return num_to_words


def get_thousands(number):
    num = int(number)
    thousands_array = []
    while num != 0:
        thousands_array.append(num % 1000)
        num /= 1000
    return thousands_array


def convert(user_input):
    int_num = int(user_input)

    if int_num < 0:
        print "منفي",
        int_num *= -1
        user_input = user_input[1:]

    if int_num < 1000:
        print less_than_thousnds(user_input)
    else:
        print greater_than_thousand(user_input)
