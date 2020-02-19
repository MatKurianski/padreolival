# Padre Olival

<img src="./screenshots/1.png"  width="240" alt="Demonstração do bot" />

Esse repositório foi um pequeno treino em Python, para auxiliar uma aposta que eu e um amigo fizemos nas férias.

Padre Olival é um bot para Telegram onde confessávamos sempre que comíamos alguma besteira ou gastavámos desnecessariamente.

Armazenamos os "pecados" usando MongoDB. Um exemplo de documento seria:

```
{
   "_id":{
      "$oid":"5e34a614adc6904feb96bb16"
   },
   "tipo":[
      "Gula",
      "Ganância"
   ],
   "nome":"Japa",
   "preço":{
      "$numberDouble":"50"
   },
   "data":{
      "$date":{
         "$numberLong":"1580508692499"
      }
   },
   "user":{
      "id":1234,
      "first_name":"Foo",
      "last_name":"Bar",
      "username":"foobar"
   }
}
```
