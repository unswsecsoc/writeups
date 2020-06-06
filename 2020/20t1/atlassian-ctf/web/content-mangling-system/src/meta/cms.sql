CREATE TABLE pages (
    id INT PRIMARY KEY,
    route TEXT UNIQUE NOT NULL,
    title TEXT NOT NULL,
    template TEXT NOT NULL,
    auth TEXT
);

INSERT INTO pages(route, title, template, auth) VALUES
('', 'Home', 'Welcome to CMS, a super light content management system. Unlike other solutions we have no passwords, no bloat and most importantly no security vulnerabilities! Click on any of the following links to try it out for yourself.<div><ul><li><a href="/blog">Blog</a></li><li><a href="/time">Time</a></li><li><a href="/hidden?token=secretpassword">Hidden Page</a></li><li><a href="/admin">Administration page (disabled)</a></li></ul></div>', NULL),
('blog', 'Blog', 'This is a example blog post. I might write about how we have the best security model ever later.', NULL),
('time', 'Time', 'We support dynamic features like time {{ time() }} and date {{ date() }}.', NULL),
('hidden', 'Hidden Page', 'This page is hidden to people without the token, remove the ?token from your url and try it for yourself', 'secretpassword'),
('admin', 'Admin Page', 'I have no idea how you got here (unless your me, in which case hi!). Anyway, heres the admin page. <div><h1>New Page</h1><style>form{width:50vw}form>div{display:grid;grid-template-columns: 1fr 1fr}</style><form action="#" method="POST"><div><label>Route</label><input type="text" name="route"></div><div><label>Title</label><input type="text" name="title"></div><div><label>Authorization <small>(leave blank for none, append <code>|admin</code> for admin)</small></label><input type="text" name="auth"></div><div><label>Template</label><textarea name="template" rows="10"></textarea></div><input type="hidden" name="token" value="{{ auth }}"><input type="submit" value="Create!"></form><div id="message"></div><script>!function(){"use strict";const e=document.querySelector("form");e.addEventListener("submit",async t=>{t.preventDefault();let n=await fetch("/api/page",{method:"POST",body:new FormData(e)}),a=await n.text(),o=document.querySelector("#message");if(n.ok){let t=document.createElement("a");o.textContent="Success! New page created at ",t.textContent="/"+a,t.href="/"+a,o.appendChild(t),e.parentElement.appendChild(o),e.reset()}else o.textContent="Failure: "+a})}();</script></div>', '5c5b07024e61e1f47641f6239be75ac112a3375b|admin')
