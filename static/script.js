const result_box = document.querySelector('.result')
const form = document.querySelector('#form')
const add_button = form.querySelector('#add-input')
const input_html = '<input class="random-list-elem" type="text">'


add_button.addEventListener('click', event => {
    event.preventDefault()
    add_button.insertAdjacentHTML('beforebegin', input_html)
})


async function handle_form(event) {
    event.preventDefault()

    let random_inputs = form.querySelectorAll('.random-list-elem')
    let random_values = []
    for (let random_input of random_inputs) {
        random_values.push(random_input.value)
        random_input.value = ''
    }
    let url = '/choice-random/'
    let shake_list = form.querySelector('#form-radio-2').checked
    if (shake_list) {
        url = '/shake-list/'
    };
    let list_object = {random_list: random_values};
    await fetch(
        url,
        {
            method: 'POST',
            headers: {'Content-Type': 'application/json;charset=utf-8'},
            body: JSON.stringify(list_object),
        },
    ).then(
        result => result.json().then(
            result => {
                console.log(result)
                result_box.innerHTML = ''
                if (shake_list) {
                    for (elem of result) {
                        result_box.insertAdjacentHTML(
                            'beforeend',
                            `<p class="randomised-elem"> ${elem['shaked']} </p>`
                        )
                    }
                }
                else {
                    result_box.insertAdjacentHTML(
                        'beforeend',
                        `<p class="randomised-elem"> ${result['choiced']} </p>`
                    )
                }
            }
        )
    )

}


form.addEventListener('submit', handle_form)
