import aiohttp
from data.config import url_edit_teacher

async def get_teacher_status(teacher_id):
    edited_url = f"{url_edit_teacher}{teacher_id}"

    async with aiohttp.ClientSession() as session:
        async with session.get(edited_url) as response:
            if response.status != 200:
                return "<b>Xatolik:</b> Serverdan ma'lumot olishda xato yuz berdi."
            status_data = await response.json()

    juda_yaxshi = sum(status_data.get(f"m{i}_juda_yaxshi", 0) or 0 for i in range(1, 7))
    yaxshi = sum(status_data.get(f"m{i}_yaxshi", 0) or 0 for i in range(1, 7))
    ortacha = sum(status_data.get(f"m{i}_ortacha", 0) or 0 for i in range(1, 7))
    past = sum(status_data.get(f"m{i}_past", 0) or 0 for i in range(1, 7))
    yomon = sum(status_data.get(f"m{i}_yomon", 0) or 0 for i in range(1, 7))

    if status_data:
        return (
            f"<b>⭐️ Sizga yangi status belgilandi!</b>\n"
            f"<pre> Juda yaxshi - {juda_yaxshi} \n"
            f" Yaxshi - {yaxshi} \n"
            f" O'rtacha - {ortacha} \n"
            f" Past - {past} \n"
            f" Yomon - {yomon}</pre>"
        )
    return "<b>Xatolik:</b> Ma'lumot topilmadi."