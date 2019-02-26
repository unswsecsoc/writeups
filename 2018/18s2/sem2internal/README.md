# Semester 2 2018 Internal CTF
Thanks to the authors, especially those who supplied challenges externally ! 
```
.
├── binary      
│   ├── adamsplayground                 (Adam Tanana)             
│   ├── copycat                         (Weilon)
│   ├── guess_my_number                 (Wing)
│   ├── hairy                           (Colin)
│   └── nethackers                      (Viv)
├── crypto
│   ├── javascrings                     (Evan)
│   ├── matrix                          (Viv)
│   ├── ptdr                            (Colin)
│   ├── rotrain                         (Evan)
│   ├── save_c3po                       (Justin Dang)
│   └── the_force_awoken                (Justin Dang)
├── forensics
│   ├── knaan                           (Evan)
│   ├── soundstorm                      (Zain)
│   └── wellmare                        (Wing)
├── README.md
├── recon
│   ├── recon_1                         (Wing)
│   └── wellmare+                       (Wing)
├── reversing
│   ├── intel_1.js                      (Zain)
│   ├── intel_2.js                      (Zain)
│   ├── intel_3.js                      (Zain)
│   └── pysafe3.0                       (Zac)
└── web
    ├── mips64me                        (Michael)
    ├── SQu1rr3L-1                      (Michael)
    └── super_secure_resource_finder    (Wing)

```

## Docker stuff
The challenges will run in Docker containers, here's some useful commands to help you run your own containers 

```
A bunch of common commands I used while setting up which you may find useful
<ID> could mean the name given (on far right column) or the hashed ID itself, both works...

docker build -t <IMG_NAME> . -- will build image based on Dockerfile
docker images -- Llist all the images currently stored on your machine, -a to view ALL
docker image prune -f -- nuke all the images
docker container ls -- see what containers are running
docker container ls -a -- list all active/inactive containers
docker contaner prune -f -- nuke all the containers
docker logs -f <ID> -- see access/error logs of that container (May help with debuging)
docker exec -it <ID> /bin/bash -- spawns a shell so you can peek it and see whats happening
docker stop <ID> -- stops the container from using the port
docker start <ID> -- restart a stopped container
docker rm <ID> -- removes the container so you can reuse the name lol

Example  (Make sure to add yourself to Docker group or just use sudo for everything lol)  
------------------------------------------------------
cd web/super_secure_resource_finder
docker build -t ssrf_image .  
docker run -d -p 9451:80 --name ssrf_app ssrf_image
curl localhost:9451     (It should return the webpage)
docker stop ssrf_app && docker rm ssrf_app && docker image rm ssrf_image (for cleanup)
------------------------------------------------------
```


