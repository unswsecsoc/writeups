(function() {
    "use strict";

    const LS_KEY = 'rss:feed';

    function closeModal() {
        Array.from(document.querySelectorAll('[data-modal]'), e => {
            Array.from(e.querySelectorAll('input, textarea')).forEach(inp => inp.value = '');
        });

        document.querySelector('#modals').classList.remove('active');
    }

    function render(store) {
        const container = document.querySelector('#subscriptions');
        const items = container.querySelectorAll('*:not(.subscription-add)');
        items.forEach(e => container.removeChild(e));

        store.forEach((e, i) => {
            let it_e = document.createElement('li');
            it_e.classList.add('subscription-item');
            it_e.setAttribute('data-sid', ''+i);
            it_e.textContent = e['name'];
            container.insertBefore(it_e, container.childNodes[0]);

            it_e.addEventListener('click', e => get_feed(i));
        });
    }

    function lsync(store, key) {
        localStorage.setItem(key, JSON.stringify(store));
    }

    let fetch_sync = null;
    let token = null;
    async function get_feed(i) {
        const data = lstore[i];
        fetch_sync = data['url'];

        let resp = await fetch('/get_feed', {
            'method': 'POST',
            'body': JSON.stringify(data),
            'headers': {'Content-Type': 'application/json'}
        });
        let content = await resp.json();
        if(content['url'] != fetch_sync) { return; }

        console.log(content, resp.ok, fetch_sync)
        const main = document.querySelector('main');
        main.innerHTML = content['content'];
        if(resp.ok) {
            main.classList.remove('has-error');
        } else {
            main.classList.add('has-error');
        }
    }

    if(!localStorage[LS_KEY]) {lsync([], LS_KEY);}

    let lstore = JSON.parse(localStorage[LS_KEY]);

    document.querySelector('#sadd').addEventListener('click', () => {
        document.querySelector('#modals').classList.add('active');
    });

    document.querySelector('#add-sub button[role="button"]').addEventListener('click', e => {
        e.preventDefault();
        closeModal();
    });

    // Begin core logic
    let form = null;
    (form = document.querySelector('#add-sub')).addEventListener('submit', e => {
        e.preventDefault();

        let data = {};
        (new FormData(form)).forEach((v, k) => data[k] = v);
        lstore.push(data);
        lsync(lstore, LS_KEY);

        render(lstore);
        closeModal();
    });

    render(lstore);
})();
