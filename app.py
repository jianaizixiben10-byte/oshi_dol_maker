import streamlit as st
import random
from pathlib import Path

st.set_page_config(
    page_title="推しドルメーカー",
    page_icon="✨",
    layout="wide"
)

BASE_DIR = Path(__file__).parent

st.markdown("""
<style>

.stApp {
    background: linear-gradient(
        135deg,
        #ff9ad5,
        #9b5cff,
        #5aa9ff
    );
}

.card {
    padding: 30px;
    border-radius: 25px;
    color: white;
    text-align: center;
    box-shadow: 0 0 25px #b266ff;
    margin-top: 20px;
    margin-bottom: 20px;
    animation: glowAnime 2s infinite alternate;
}

.title {
    font-size: 42px;
    font-weight: bold;
    color: white;
}

.sub {
    font-size: 24px;
    color: white;
    margin-bottom: 15px;
}

@keyframes glowAnime {
    from {
        transform: scale(1);
    }

    to {
        transform: scale(1.02);
    }
}

</style>
""", unsafe_allow_html=True)

st.title("推しドルメーカー")
st.write("あなたを韓国アイドル化する診断アプリです！")

# 初期設定
if "fans" not in st.session_state:
    st.session_state.fans = 100
if "favor" not in st.session_state:
    st.session_state.favor = 50
if "level" not in st.session_state:
    st.session_state.level = 1
if "logs" not in st.session_state:
    st.session_state.logs = []
if "outfit_level" not in st.session_state:
    st.session_state.outfit_level = 1
if "outfits" not in st.session_state:
    st.session_state.outfits = []

tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "診断",
    "育成",
    "衣装",
    "エンディング",
    "ログ"
])

with tab1:
    nickname = st.text_input("ニックネームを入力してください")

    color = st.selectbox(
        "好きな色を選んでください",
        ["ピンク", "ブルー", "パープル", "ブラック", "ホワイト"]
    )

    personality = st.selectbox(
        "あなたの性格を選んでください",
        ["明るい", "クール", "天然", "努力家", "ミステリアス"]
    )

    vibe = st.selectbox(
        "なりたい雰囲気を選んでください",
        ["かわいい", "かっこいい", "清楚", "カリスマ", "大人っぽい"]
    )

    if st.button("診断する"):
        idol_names = ["LUNA", "ARIA", "YUNA", "MIRA", "SENA"]
        group_names = ["NEON SKY", "LUVIX", "VELUNA", "STARGLOW", "MOONIX"]
        positions = ["メインボーカル", "リーダー", "メインダンサー", "ラッパー", "センター"]
        fandom_names = ["LUMIES", "STARZY", "MOONLIGHT", "VELUV", "NEOZ"]
        album_names = ["ECLIPSE", "MIDNIGHT PINK", "GALAXY LOVE", "NEON HEART", "BLACK ROSE"]
        concept_titles = ["Moonlight Version", "Black Swan Concept", "Neon Dream Ver.", "Midnight Angel", "Galaxy Princess"]
        rarities = ["N", "R", "SR", "SSR", "UR"]

        catchphrases = [
            "月明かりのように輝くカリスマ",
            "世界を魅了する透明感アイドル",
            "視線を奪う最強センター",
            "クールで美しいパフォーマー",
            "ファンを笑顔にする天才アイドル"
        ]

        habits = [
            "今日も一緒に輝こう！",
            "みんな愛してるよ♡",
            "最高のステージにしよう！",
            "君だけを見てるよ！",
            "もっと会いに来てね！"
        ]

        histories = [
            "2023年：韓国事務所にスカウトされた",
            "2024年：練習生としてデビュー準備開始",
            "2025年：音楽番組で新人賞を受賞",
            "2026年：世界ツアーが決定",
            "2027年：SNSフォロワー1000万人突破"
        ]

        rare_effects = [
            "✨SSRアイドル爆誕✨",
            "🌟伝説級センター誕生🌟",
            "💜神ビジュアル確定💜",
            "👑ワールドスター候補👑",
            "🔥ステージ支配者タイプ🔥"
        ]

        idol_types = [
            "クール系エース",
            "愛されマンネ",
            "カリスマリーダー",
            "ギャップ天才",
            "セクシーパフォーマー"
        ]

        if nickname.strip() == "":
            display_name = f"{random.choice(idol_names)}"
        else:
            idol_name = random.choice(idol_names)
            display_name = f"{nickname} from {idol_name}"

        data = {
            "display_name": display_name,
            "group_name": random.choice(group_names),
            "position": random.choice(positions),
            "fandom_name": random.choice(fandom_names),
            "album_name": random.choice(album_names),
            "concept_title": random.choice(concept_titles),
            "color": color,
            "personality": personality,
            "vibe": vibe,
            "rarity": random.choice(rarities),
            "rare_effect": random.choice(rare_effects),
            "catchphrase": random.choice(catchphrases),
            "habit": random.choice(habits),
            "history": random.choice(histories),
            "idol_type": random.choice(idol_types)
        }

        st.session_state.result = data

    if "result" in st.session_state:
        result = st.session_state.result

        bg_colors = {
            "ピンク": "#ff8fc7",
            "ブルー": "#5aa9ff",
            "パープル": "#9b5cff",
            "ブラック": "#222222",
            "ホワイト": "#cccccc"
        }

        bg_color = bg_colors[result["color"]]

        if result["rarity"] in ["SSR", "UR"]:
            glow = "0 0 40px gold"
        else:
            glow = "0 0 25px #b266ff"

        st.subheader("診断結果")

        st.markdown(f"""
<div class="card" style="background-color:{bg_color}; box-shadow:{glow};">
<div style="background: rgba(255,255,255,0.15); padding:20px; border-radius:20px; backdrop-filter: blur(10px);">

<div class="title">{result["display_name"]}</div>
<div class="sub">{result["position"]}</div>

<p>所属グループ：{result["group_name"]}</p>
<p>ファンダム名：{result["fandom_name"]}</p>
<p>デビューアルバム：{result["album_name"]}</p>
<p>コンセプトフォト：{result["concept_title"]}</p>

<hr>

<p>推しカラー：{result["color"]}</p>
<p>性格：{result["personality"]}</p>
<p>雰囲気：{result["vibe"]}</p>
<h2>【{result["rarity"]}】</h2>
<h3>{result["rare_effect"]}</h3>
<p>{result["catchphrase"]}</p>
<p>「{result["habit"]}」</p>
<p>{result["history"]}</p>
<p>アイドルタイプ：{result["idol_type"]}</p>

</div>
</div>
""", unsafe_allow_html=True)

        if result["rarity"] == "N":
            image_file = "idol_n.png"
        elif result["rarity"] == "R":
            image_file = "idol_r.png"
        elif result["rarity"] == "SR":
            image_file = "idol_sr.png"
        elif result["rarity"] == "SSR":
            image_file = "idol_ssr.png"
        else:
            image_file = "idol_ur.png"

        image_path = BASE_DIR / image_file

        if image_path.exists():
            st.image(str(image_path), width=320)
        else:
            st.warning(f"{image_file} が見つかりません。app.py と同じフォルダに画像を置いてください。")

        share_text = f"""私の韓国アイドル化診断結果は…

✨ {result["display_name"]} ✨
ポジション：{result["position"]}
所属グループ：{result["group_name"]}
ファンダム名：{result["fandom_name"]}
デビューアルバム：{result["album_name"]}
コンセプトフォト：{result["concept_title"]}
推しカラー：{result["color"]}
雰囲気：{result["vibe"]}

{result["rare_effect"]}

#推しドルメーカー
#韓国アイドル化診断
"""
        st.text_area("SNSシェア用テキスト", share_text, height=180)

with tab2:
    st.subheader("現在のステータス")

    if st.session_state.level == 1:
        rank = "練習生"
    elif st.session_state.level == 2:
        rank = "新人アイドル"
    elif st.session_state.level == 3:
        rank = "人気アイドル"
    elif st.session_state.level == 4:
        rank = "トップスター"
    else:
        rank = "ワールドスター"

    if st.session_state.fans >= 5000:
        title = "🌍 伝説のワールドスター"
    elif st.session_state.fans >= 2000:
        title = "👑 トップスター"
    elif st.session_state.fans >= 1000:
        title = "🌟 人気急上昇アイドル"
    elif st.session_state.fans >= 500:
        title = "🎤 注目の新人"
    else:
        title = "✨ 期待の練習生"

    st.write(f"ファン数：{st.session_state.fans}人")
    st.write(f"好感度：{st.session_state.favor}")
    st.write(f"レベル：{st.session_state.level}")
    st.write(f"アイドルランク：{rank}")
    st.write(f"称号：{title}")
    st.write(f"衣装レベル：{st.session_state.outfit_level}")

    st.subheader("人気ステータス")
    st.write("人気度")
    st.progress(min(st.session_state.fans / 5000, 1.0))
    st.write("好感度")
    st.progress(min(st.session_state.favor / 100, 1.0))

    if st.button("今日の活動をする"):
        good_events = [
            "ライブが大成功した！",
            "ファンサが神対応すぎてバズった！",
            "空港ファッションが話題になった！",
            "TikTok動画が100万再生された！",
            "ダンス動画が韓国でトレンド入り！"
        ]

        bad_events = [
            "寝坊してレッスンに遅刻した…",
            "SNS投稿を誤爆して炎上した！",
            "熱愛報道が出てファンがざわついた！",
            "生配信で転んでしまった！",
            "ダンスを間違えてしまった！"
        ]

        if random.choice(["good", "bad"]) == "good":
            event = random.choice(good_events)
            st.session_state.fans += random.randint(50, 300)
            st.session_state.favor += random.randint(1, 10)
            st.success(event)
        else:
            event = random.choice(bad_events)
            st.session_state.fans = max(0, st.session_state.fans - random.randint(20, 100))
            st.session_state.favor = max(0, st.session_state.favor - random.randint(1, 5))
            st.error(event)

        st.session_state.logs.append(event)

    if st.session_state.fans >= 2000 and st.session_state.level < 4:
        st.session_state.level = 4
        st.balloons()
        st.success("👑 トップスター達成！")
    elif st.session_state.fans >= 1000 and st.session_state.level < 3:
        st.session_state.level = 3
        st.balloons()
        st.success("🌟 人気アイドルになった！")
    elif st.session_state.fans >= 500 and st.session_state.level < 2:
        st.session_state.level = 2
        st.balloons()
        st.success("🎉 新人アイドルに昇格した！")

    st.subheader("ログインボーナス")

    if st.button("ログインボーナスを受け取る"):
        rewards = [
            "💎 ダイヤ100個獲得！",
            "👗 限定ステージ衣装を入手！",
            "🔥 ファンが500人増加！",
            "🎤 ボーカル力アップ！",
            "🌟 SNSでトレンド入り！"
        ]

        reward = random.choice(rewards)
        st.success(reward)
        st.session_state.fans += random.randint(50, 500)
        st.session_state.logs.append(reward)

    st.subheader("SNS投稿")

    if st.button("SNSに投稿する"):
        posts = [
            "自撮りがバズった！",
            "ダンス動画が急上昇入り！",
            "ファンアートが大量に投稿された！",
            "コメント返しで好感度アップ！"
        ]

        post = random.choice(posts)
        st.success(post)
        st.session_state.fans += random.randint(100, 600)
        st.session_state.favor += random.randint(5, 15)
        st.session_state.logs.append(post)

    st.subheader("レッスン")

    if st.button("レッスンを受ける"):
        lessons = [
            "ボーカル力が上がった！",
            "ダンスがキレキレになった！",
            "表情管理が上達した！",
            "ラップスキルが成長した！"
        ]

        lesson = random.choice(lessons)
        st.success(lesson)
        st.session_state.favor += random.randint(3, 10)
        st.session_state.logs.append(lesson)

    st.subheader("スキャンダル対応")

    if st.button("スキャンダル対応をする"):
        scandals = [
            "神対応で好感度が回復した！",
            "誠実なコメントでファンが増えた！",
            "少し炎上してしまった…",
            "沈黙を守って話題が落ち着いた。"
        ]

        scandal = random.choice(scandals)
        st.write(scandal)

        if "回復" in scandal or "増えた" in scandal:
            st.success("イメージアップ成功！")
            st.session_state.favor += random.randint(10, 25)
            st.session_state.fans += random.randint(100, 300)
        else:
            st.error("少しイメージダウン…")
            st.session_state.favor = max(0, st.session_state.favor - random.randint(5, 15))

        st.session_state.logs.append(scandal)

    st.subheader("ライブツアー")

    if st.button("ライブツアーを開催する"):
        tours = [
            "🇰🇷 ソウルアリーナ公演が満員！",
            "🇯🇵 東京ドームライブ大成功！",
            "🇺🇸 LAライブで海外人気爆発！",
            "🇫🇷 パリ公演でファンが熱狂！",
            "🇹🇭 バンコク公演でトレンド1位！"
        ]

        tour_result = random.choice(tours)
        st.success(tour_result)
        st.session_state.fans += random.randint(300, 1000)
        st.session_state.favor += random.randint(5, 20)
        st.session_state.logs.append(tour_result)

with tab3:
    st.subheader("衣装ガチャ")

    if st.button("衣装ガチャを引く"):
        outfits = [
            "👼 天使コンセプト衣装",
            "🖤 ブラックドレス衣装",
            "🎀 ピンクリボン衣装",
            "⚡ サイバーパンク衣装",
            "👑 女王様ステージ衣装",
            "🌙 月光プリンセス衣装"
        ]

        outfit = random.choice(outfits)

        if outfit in st.session_state.outfits:
            st.info(f"{outfit} はすでに持っています。かぶりボーナスでファンが100人増えました！")
            st.session_state.fans += 100
            st.session_state.logs.append(f"{outfit} がかぶったのでファンが100人増えた！")
        else:
            st.success(f"{outfit} をゲットしました！")
            st.session_state.outfits.append(outfit)
            st.session_state.favor += random.randint(3, 15)
            st.session_state.logs.append(outfit)

    st.subheader("衣装レベルアップ")

    if st.button("衣装をレベルアップする"):
        st.session_state.outfit_level += 1
        st.session_state.favor += 10
        st.session_state.fans += 200

        message = f"衣装レベルが {st.session_state.outfit_level} になった！"
        st.success(message)
        st.session_state.logs.append(message)

    st.subheader("所持衣装コレクション")

    if len(st.session_state.outfits) == 0:
        st.write("まだ衣装を持っていません。衣装ガチャを引いてみよう！")
    else:
        for outfit in st.session_state.outfits:
            st.write(f"・{outfit}")

with tab4:
    st.subheader("エンディング")

    if st.session_state.fans >= 5000:
        st.balloons()
        st.success("🎉 ワールドツアー成功！あなたは伝説のK-POPアイドルになりました！")
        st.write("ここまで育成してくれてありがとう！")
    else:
        st.write("ファン数5000人を目指して、さらに活動しよう！")

with tab5:
    st.subheader("活動ログ")

    if len(st.session_state.logs) == 0:
        st.write("まだ活動ログはありません。")
    else:
        for log in st.session_state.logs:
            st.write(f"・{log}")

    st.subheader("リセット")

    if st.button("最初から育成する"):
        st.session_state.fans = 100
        st.session_state.favor = 50
        st.session_state.level = 1
        st.session_state.outfit_level = 1
        st.session_state.outfits = []
        st.session_state.logs = []

        if "result" in st.session_state:
            del st.session_state.result

        st.success("育成データをリセットしました！")