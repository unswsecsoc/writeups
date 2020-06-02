(function() {
    "use strict";

    async function decryption_prompt(e) {
        // You can see my regret in not properly desigining the UI here
        let user_key = prompt("Decryption Key");
        if(!user_key || (user_key = try_atob(user_key)) === null || user_key.length != 32) {
            alert('Invalid key');
            return false;
        }

        let content = e.getAttribute('data-content');
        if(!content || (content = try_atob(content)) === null) {
            alert('Invalid Content');
            return false;
        }

        const iv  = to_byte_array(user_key.slice(0, 16));
        const key = to_byte_array(user_key.slice(16));

        let decrypted = null;
        try {
            const cbc = new aesjs.ModeOfOperation.cbc(key, iv);
            decrypted = cbc.decrypt(to_byte_array(content));
        } catch {
            alert('Could not decrypt');
            return;
        }

        alert(`Decrypted: ${from_bytes(decrypted)}`);
    }

    const LS_KEY = 'sprout:messages';
    if(localStorage[LS_KEY] === undefined) {
        localStorage[LS_KEY] = '[]';
    }

    function prettify_time(ts) {
        return new Date(+ts).toLocaleString();
    }

    function table_row(content) {
        const tr = document.createElement('tr');
        const td = ["name", "content", "time"].map(l => {
            let td = document.createElement('td');
            td.textContent = content[l];
            return td;
        })
        const decrypt = document.createElement('td');
        const decrypt_link = document.createElement('a');

        decrypt_link.textContent = 'Decrypt';
        decrypt_link.href = '#';
        decrypt_link.setAttribute('data-content', content['content']);
        decrypt_link.addEventListener('click', async () => decryption_prompt(decrypt_link));

        td[2].textContent = prettify_time(td[2].textContent);

        td.forEach(t => tr.appendChild(t));
        decrypt.appendChild(decrypt_link);
        tr.appendChild(decrypt);

        return tr;
    }

    function show_key(key) {
        document.querySelector('#key').textContent = key;
        document.querySelector('#enckey').classList.remove('is-hidden');
    }

    function push_ls(content) {
        let messages = JSON.parse(localStorage[LS_KEY]);
        messages.push(content);
        localStorage[LS_KEY] = JSON.stringify(messages);
    }

    const messages = document.querySelector('#messages');
    Array.from(messages.querySelectorAll('tbody td:nth-child(3)')).forEach(e => {
        e.textContent = prettify_time(e.textContent.trim());
    });

    document.querySelector('form').addEventListener('submit', async function(e) {
        e.preventDefault();

        const resp = await fetch('/encrypt', {
            body: new FormData(this),
            method: 'POST'
        });
        const content = await resp.json();

        show_key(content['key']);
        delete content['key'];

        messages.querySelector('tbody').appendChild(table_row(content));

        push_ls(content);
    });

    function try_atob(b64) {
        try { return atob(b64); }
        catch { return null; }
    }

    function to_byte_array(str) {
        return new Uint8Array(str.split('').map(c => c.charCodeAt(0)));
    }

    function from_bytes(arr) {
        return aesjs.utils.utf8.fromBytes(arr);
    }

    Array.from(document.querySelectorAll('a[href="#"]')).forEach(e => e.addEventListener('click', async () => decryption_prompt(e)));

    JSON.parse(localStorage[LS_KEY]).forEach(entry => {
        messages.querySelector('tbody').appendChild(table_row(entry));
    });
})();
