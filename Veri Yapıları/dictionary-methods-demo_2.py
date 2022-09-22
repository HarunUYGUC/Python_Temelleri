"""
    player 1: 
        id             => 1
        name           => Cristiano Ronaldo
        yearOfBirth    => 1985
        nationality    => Portugal
        current_team   => Portugal
        history        => Juventus, Real Madrid, Portugal

    player 2:
        id             => 2
        name           => Lionel Messi
        yearOfBirth    => 1987
        nationality    => Argentina
        current_team   => Barcelona
        history        => Barcelona, Argentina, Portugal
"""

id = input("Oyuncunun ID'sini giriniz : ")
name = input("Oyuncunun ADINI giriniz : ")
yearOfBirth = input("Oyuncunun DOĞUM YILINI giriniz : ")
nationality = input("Oyuncunun ÜLKESİNİ giriniz : ")
current_team = input("Oyuncunun MEVCUT TAKIMINI giriniz : ")
history = input("Oyuncunun OYNADIĞI TAKIMLARI giriniz : ")


players = {
    id: {
        "Ad": name,
        "Doğum Yılı": yearOfBirth,
        "Ülkesi": nationality,
        "Mevcut Takımı": current_team,
        "Oynadığı Takımlar": history.split(",")
    }
}

print(players)

id = input("Oyuncunun ID'sini giriniz : ")
name = input("Oyuncunun ADINI giriniz : ")
yearOfBirth = input("Oyuncunun DOĞUM YILINI giriniz : ")
nationality = input("Oyuncunun ÜLKESİNİ giriniz : ")
current_team = input("Oyuncunun MEVCUT TAKIMINI giriniz : ")
history = input("Oyuncunun OYNADIĞI TAKIMLARI giriniz : ")

players.update({
    id: {
        "Ad": name,
        "Doğum Yılı": yearOfBirth,
        "Ülkesi": nationality,
        "Mevcut Takımı": current_team,
        "Oynadığı Takımlar": history
    }
})

print(players)