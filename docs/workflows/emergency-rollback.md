# Workflow: Emergency Rollback

## เมื่อไหร่ต้อง trigger rollback

- แอปรันไม่ได้หลัง update
- หน้าเว็บขาวหรือ error 500 ที่ผู้ใช้เห็น
- ข้อมูลผู้ใช้เสียหาย
- เผลอสั่งงานที่อันตราย
- มี secret/API key หลุด
- deploy แล้วผู้ใช้เจอปัญหา

## 1. สิ่งที่เจ้าของต้อง "ห้ามทำ"

- ห้ามบังคับ restart/app โดยไม่แจ้ง Cline
- ห้ามแก้โค้ดเอง
- ห้ามลบไฟล์
- ห้าม force push หรือ reset --hard
- ห้ามแก้ไข database จริง

## 2. ข้อมูลที่ควรเก็บ

- ข้อความ error ที่เห็น
- รูป/ภาพหน้าจอ
- วันที่-เวลาที่เกิด
- สิ่งที่ทำก่อนที่จะพัง
- ข้อมูลที่อาจเกี่ยวกับ secret ที่หลุด (แต่ห้ามแปะใน chat/docs)

## 3. Prompt ที่ส่ง Cline ได้ทันที

```
อ่าน docs/HANDOFF.md, docs/CURRENT_TASK.md, docs/04_DECISIONS.md

สถานการณ์ฉุกเฉิน: [บรรยายสั้น ๆ ว่าเกิดอะไรขึ้น]

สิ่งที่สังเกตได้:
- [ข้อความ error]
- [สิ่งที่เกิดขึ้น]

ห้ามทำอะไรที่เสี่ยง:
- ห้ามแก้ database
- ห้ามลบไฟล์
- ห้าม commit ตอนนี้

ฉันต้องการ rollback ไปยัง commit ก่อนหน้า
```

## 4. เกณฑ์ว่าเมื่อใดต้องหยุด deploy/rollback

- ถ้าไม่แน่ใจ → หยุด, อย่าทำอะไรเพิ่ม, ส่ง prompt ให้ Cline
- ถ้ามี secret หลุด → หยุดใช้งาน, แจ้ง Cline ทันที, ห้ามแปะ secret ลง chat
- ถ้า app crash ไม่ได้ → หยุดใช้งาน, ส่งข้อความให้ Cline

## 5. Rollback verification

- ตรวจสอบว่า rollback สำเร็จ (app เปิดได้, ทำงานได้)
- ตรวจสอบไฟล์ที่เปลี่ยนด้วย `git diff`
- อัปเดต `docs/HANDOFF.md` ให้เป็นปัจจุบัน
- อัปเดต `docs/CHANGELOG.md` ระบุ rollback

## 6. Post-incident documentation

- บันทึกสิ่งที่เกิดใน `docs/CHANGELOG.md`
- บันทึก root cause ใน `docs/04_DECISIONS.md`
- บันทึกบทเรียนใน `docs/05_BACKLOG.md`

## 7. Follow-up actions

- ตรวจสอบว่า secret หลุดไปถึงที่ไหนบ้าง (ถ้าเกิดขึ้น)
- เพิ่ม automated test หากพบจุดอ่อน
- อัปเดต emergency procedure ตามบทเรียน