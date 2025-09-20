# (Uncle Chat) Free Chat Rooms by Uncle Engineer

PyPI: https://pypi.org/project/unclechat/

โปรแกรมแชทนี้เป็นโปรแกรมที่ลุงเขียนขึ้นมาโดยใช้ Python และไลบรารี่ Socket สำหรับใช้งานในการแชทอย่างรวดเร็ว เพียงแค่มี Python อยู่ในคอมพิวเตอร์ก็สามารถใช้งานได้เลย เบื้องหลังการทำงานลุงมีโปรแกรมฝั่ง Server รันอยู่บน Server ลุง สำหรับคอยรับส่งข้อมูลต่อไปยังผู้ใช้งานตามห้องต่างๆที่สร้างขึ้น 

หากใครต้องการเรียนพื้นฐานเรื่อง Python Socket ลุงได้สอนไปอย่างละเอียดระดับหนึ่ง ดูวิดีโอสอนได้ตามลิ้งค์ยูทูปช่องลุง: https://youtu.be/MEaEVF3ZWfE (ยาว 8 ชั่วโมง 38 นาที) ---> ฝากกด Subscribe ด้วยจ่ะ!

ปล. เวอร์ชั่นนี้ยังไม่สมบูรณ์ (เขียนแบบรีบๆ 55) ลุงเขียนขึ้นมาเพื่อประยุกต์นำ Python + Socket Library สร้างเป็นโปรแกรมแชทตัวอย่าง สำหรับนักพัฒนาสามารถนำ Source Code ไปพัฒนาต่อได้เต็มที่

### วิธีติดตั้ง

เปิด CMD / Terminal

```python
pip install unclechat
```

### วิธีใช้

[STEP 1]
- เปิด IDLE ขึ้นมาแล้วพิมพ์...

```python
import unclechat
```

- หรือเปิด cmd / terminal แล้วพิมพ์

```python
python -m unclechat
```

[STEP 2]
- กรอกชื่อผู้ใช้งานในช่อง Name
- กด Enter Chatroom เพื่อเข้าห้องแชทรวม (เลขห้องแชทรวมคือ 10001)

หากต้องการสร้างห้องใหม่
- กด New Room
- โปรแกรมจะสร้างห้องให้อัตโนมัติ (จำเลขห้องไว้ส่งให้เพื่อน)
- กด Enter Chatroom เพื่อเริ่มแชท

[STEP 3]
- ใช้งานได้เลยจ้าาา หากมีการกดปิดโปรแกรมระบบจะแจ้งให้สมาชิกท่านอื่นทราบว่าผู้ใช้ได้ออกจากกลุ่มแล้ว

พัฒนาโดย: ลุงวิศวกร สอนคำนวณ
FB: https://www.facebook.com/UncleEngineer
YouTube: https://www.youtube.com/UncleEngineer

----------คำอธิบายเพิ่มเติมโดย AI----------
# UncleChat 💬

**Free Chat Rooms by Uncle Engineer**

โปรแกรมแชทแบบ real-time ที่พัฒนาด้วย Python Socket Programming สำหรับการเรียนรู้และใช้งานจริง

[![PyPI](https://img.shields.io/badge/PyPI-unclechat-blue)](https://pypi.org/project/unclechat/)
[![Python](https://img.shields.io/badge/Python-3.x-green)](https://python.org)
[![License](https://img.shields.io/badge/License-Open%20Source-yellow)](https://github.com/UncleEngineer/UncleChat)

## 📖 ภาพรวม

UncleChat เป็นโปรแกรมแชทที่พัฒนาโดยลุงวิศวกร โดยใช้เทคโนโลยี Python Socket Programming เป็นหลัก ออกแบบมาเพื่อให้ผู้ใช้สามารถสร้างและเข้าร่วมห้องแชทได้อย่างง่ายดาย พร้อมทั้งเป็นตัวอย่างการใช้งาน Socket Programming ในทางปฏิบัติ

### ✨ คุณสมบัติหลัก

- 🚀 **ใช้งานง่าย**: เพียงติดตั้ง Python ก็สามารถใช้งานได้ทันที
- 🏠 **ระบบห้องแชท**: รองรับการสร้างห้องแชทหลายห้อง
- 👥 **Multi-user**: รองรับผู้ใช้หลายคนในห้องเดียวกัน
- ⚡ **Real-time**: ส่งและรับข้อความแบบ real-time
- 🔒 **Room ID**: ระบบหมายเลขห้องสำหรับความปลอดภัย
- 📱 **Cross-platform**: ใช้งานได้บน Windows, macOS, Linux

## 🛠️ เทคโนโลยีที่ใช้

### Architecture
```
┌─────────────┐    Socket Connection    ┌─────────────┐
│   Client    │ ◄─────────────────────► │   Server    │
│  (Your PC)  │                         │ (Uncle's)   │
└─────────────┘                         └─────────────┘
       ▲                                       ▲
       │                                       │
       ▼                                       ▼
┌─────────────┐                         ┌─────────────┐
│    GUI      │                         │ Room Mgmt   │
│ (Tkinter)   │                         │ Multi-thread│
└─────────────┘                         └─────────────┘
```

### Core Technologies
- **Python Socket Library**: การสื่อสารระหว่าง client-server
- **TCP Protocol**: การส่งข้อมูลที่เชื่อถือได้
- **Multi-threading**: จัดการผู้ใช้หลายคนพร้อมกัน
- **Tkinter GUI**: ส่วนติดต่อผู้ใช้

## 📦 การติดตั้ง

### ขั้นตอนที่ 1: ติดตั้งผ่าน pip

```bash
pip install unclechat
```

### ขั้นตอนที่ 2: เริ่มใช้งาน

**วิธีที่ 1: ผ่าน Python**
```python
import unclechat
```

**วิธีที่ 2: ผ่าน Command Line**
```bash
python -m unclechat
```

## 🚀 วิธีใช้งาน

### การเข้าห้องแชทรวม

1. **เริ่มโปรแกรม**: รันคำสั่งตามขั้นตอนติดตั้ง
2. **กรอกชื่อ**: ใส่ชื่อผู้ใช้งานในช่อง Name
3. **เข้าห้องรวม**: กด Enter Chatroom (ห้องรวม ID: 10001)
4. **เริ่มแชท**: พิมพ์ข้อความและส่งได้เลย

### การสร้างห้องใหม่

1. **สร้างห้อง**: กดปุ่ม "New Room"
2. **รับ Room ID**: ระบบจะสร้างหมายเลขห้องให้อัตโนมัติ
3. **แชร์เพื่อน**: ส่งหมายเลขห้องให้เพื่อนเพื่อเข้าร่วม
4. **เข้าห้อง**: กด Enter Chatroom เพื่อเริ่มแชท

### ตัวอย่างการใช้งาน

```
┌─────────────────────────────────────┐
│          UncleChat v1.0             │
├─────────────────────────────────────┤
│ Name: [John_Doe____________]        │
│ Room: [10001_______________]        │
│                                     │
│ [Enter Chatroom] [New Room]         │
├─────────────────────────────────────┤
│ Chat History:                       │
│ System: Welcome to UncleChat!       │
│ Alice: สวัสดีครับ                    │
│ Bob: Hello everyone!                │
│ You: ยินดีที่ได้รู้จักครับ             │
├─────────────────────────────────────┤
│ Message: [พิมพ์ข้อความ...___] [Send] │
└─────────────────────────────────────┘
```

## 🔧 ตัวอย่างโค้ด Socket Programming

### Client Side (Simplified)
```python
import socket

# สร้าง socket connection
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# เชื่อมต่อไปยัง server
server_host = 'uncle-server.com'
server_port = 8080
client_socket.connect((server_host, server_port))

# ส่งข้อความ
message = "สวัสดีครับ!"
client_socket.send(message.encode('utf-8'))

# รับข้อความ
response = client_socket.recv(1024)
print(response.decode('utf-8'))

client_socket.close()
```

### Server Side (Simplified)
```python
import socket
import threading

def handle_client(client_socket, room_id):
    while True:
        try:
            message = client_socket.recv(1024)
            if message:
                # ส่งต่อไปยัง clients อื่นในห้องเดียวกัน
                broadcast_message(message, room_id, client_socket)
            else:
                break
        except:
            break
    
    client_socket.close()

# สร้าง server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 8080))
server_socket.listen(5)

while True:
    client_socket, address = server_socket.accept()
    client_thread = threading.Thread(
        target=handle_client, 
        args=(client_socket, room_id)
    )
    client_thread.start()
```

## 📚 การเรียนรู้เพิ่มเติม

### วิดีโอสอน Python Socket Programming
🎥 **คอร์สสอนครบครัน 8+ ชั่วโมง**
- [Python Socket Programming by Uncle Engineer](https://youtu.be/MEaEVF3ZWfE)
- เนื้อหาครอบคลุม: Socket basics, TCP/UDP, Multi-threading, Error handling

### หัวข้อที่ควรศึกษา
1. **Socket Fundamentals**
   - TCP vs UDP protocols
   - Client-Server architecture
   - Address families (AF_INET, AF_INET6)

2. **Advanced Topics**
   - Multi-threading for concurrent connections
   - Error handling and exception management
   - Security considerations (SSL/TLS)

3. **GUI Development**
   - Tkinter basics
   - Event-driven programming
   - Threading in GUI applications

## 🛡️ ข้อควรระวัง

### Security Notes
- โปรแกรมนี้เป็นตัวอย่างเพื่อการเรียนรู้
- ไม่ควรใช้ส่งข้อมูลที่เป็นความลับ
- ในการใช้งานจริงควรเพิ่ม encryption

### Performance Notes
- เหมาะสำหรับการใช้งานขนาดเล็กถึงกลาง
- สำหรับ production ควรพิจารณา WebSocket หรือ frameworks อื่น

## 🔧 การพัฒนาต่อ

### โครงสร้างโปรเจกต์แนะนำ
```
unclechat/
├── client/
│   ├── gui.py          # Tkinter GUI
│   ├── socket_client.py # Socket client logic
│   └── utils.py        # Helper functions
├── server/
│   ├── server.py       # Main server
│   ├── room_manager.py # Room management
│   └── client_handler.py # Client handling
├── common/
│   ├── protocol.py     # Message protocol
│   └── constants.py    # Shared constants
└── tests/
    ├── test_client.py
    └── test_server.py
```

### Features ที่สามารถเพิ่มได้
- 📁 File sharing
- 🎨 Message formatting (bold, italic)
- 📷 Image sharing
- 🔐 Password-protected rooms
- 📱 Mobile app version
- 🌐 Web interface
- 💾 Message history
- 👤 User profiles

## 🤝 การสนับสนุน

### ช่องทางติดต่อ
- **Facebook**: [Uncle Engineer](https://www.facebook.com/UncleEngineer)
- **YouTube**: [Uncle Engineer Channel](https://www.youtube.com/UncleEngineer)
- **Website**: Uncle-engineer.com

### การมีส่วนร่วม
- 🐛 รายงาน bug ผ่าน GitHub Issues
- 💡 เสนอ feature ใหม่
- 🔧 ส่ง Pull Request
- 📚 ปรับปรุงเอกสาร

## 📄 License

โปรเจกต์นี้เป็น Open Source สามารถนำไปใช้และพัฒนาต่อได้อย่างเต็มที่

## 🙏 ขอบคุณ

ขอบคุณลุงวิศวกรสำหรับการสร้างโปรแกรมนี้เพื่อการเรียนรู้ และขอบคุณชุมชน Python ที่ทำให้ Socket Programming เข้าถึงได้ง่าย

---

**หมายเหตุ**: โปรเจกต์นี้ยังอยู่ระหว่างการพัฒนา (เขียนแบบรีบๆ 😅) และเปิดรับการพัฒนาต่อจากชุมชน

**สร้างด้วย ❤️ โดยลุงวิศวกร และชุมชน Python Thailand**

