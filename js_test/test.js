
import fetch from 'node-fetch';

const newPost = {
  title: 'foo',
  body: 'bar',
  userId: 1,
}

fetch('http://127.0.0.1:5000/', {
  method: 'POST', // Здесь так же могут быть GET, PUT, DELETE
  body: JSON.stringify(newPost), // Тело запроса в JSON-формате
  headers: {
    // Добавляем необходимые заголовки
    'Content-type': 'application/json; charset=UTF-8',
  },
})
  .then((response) => response.json())
  .then((data) => {
    console.log(data)
    // {title: "foo", body: "bar", userId: 1, id: 101}
  })

