import requests

if __name__ == "__main__":
    url: str = "http://localhost:8000/analyze_text"
    data: dict[str, str] = {"text": "Ублюдок, мать твою, а ну, иди сюда, говно собачье, а? Сдуру решил ко мне лезть, ты? "
                                    "Засранец вонючий, мать твою, а? Ну, иди сюда, попробуй меня трахнуть — я тебя сам "
                                    "трахну, ублюдок, онанист чёртов, будь ты проклят! Иди, идиот, трахать тебя и всю "
                                    "твою семью! Говно собачье, жлоб вонючий, дерьмо, сука, падла! Иди сюда, мерзавец, "
                                    "негодяй, гад! Иди сюда, ты, говно, жопа!"}
    headers: dict[str, str] = {"Content-Type": "application/json"}
    response: requests.post = requests.post(url, json=data, headers=headers)

    print(response.json())
