# Security and Data Safety

- ห้ามเปิดเผย, log, commit หรือใส่ secret/API key/password/token/PII ลง docs หรือ source code
- ตรวจ environment variable จาก .env.example หรือ config template เท่านั้น
- ห้ามแก้ production database หรือรัน destructive command โดยไม่มี approval ชัดเจน
- การเปลี่ยน database schema ต้องระบุ migration plan, rollback plan และผลกระทบก่อน
- งาน auth, role, permission, payment, webhook, upload, user data หรือ admin action เป็น high-risk
- งาน high-risk ต้องเสนอแผนและรออนุมัติก่อน implement
- ตรวจ input validation, authorization และ error handling ตามขอบเขตงาน
- ห้ามอ้างว่า secure หรือ production-ready หากยังไม่ได้ตรวจสอบจริง
- หากพบ secret ใน repository ให้หยุดและรายงาน ห้ามแปะค่า secret ซ้ำในคำตอบหรือเอกสาร