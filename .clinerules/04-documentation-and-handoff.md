# Documentation and Handoff

หลังจบทุก task:

1. อัปเดต docs/CURRENT_TASK.md
2. อัปเดต docs/HANDOFF.md
3. อัปเดต docs/05_BACKLOG.md หากพบงานต่อเนื่อง
4. อัปเดต docs/04_DECISIONS.md หากมี decision ถาวรจริง
5. อัปเดต docs/01_REQUIREMENTS.md หาก business rule เปลี่ยน
6. อัปเดต docs/02_ARCHITECTURE.md หาก architecture/API/schema/dependency เปลี่ยน
7. อัปเดต docs/CHANGELOG.md หากมี behavior ที่ผู้ใช้เห็นหรือมี release-worthy change

กติกาเอกสาร:

- HANDOFF คือสถานะปัจจุบัน ไม่ใช่ transcript การคุย
- DECISIONS เก็บเฉพาะสิ่งที่ตัดสินใจแล้ว ไม่ใช่ข้อเสนอ
- CURRENT_TASK มีได้หนึ่งงานหลักที่ active ในเวลาเดียวกัน
- BACKLOG ต้องแยก priority และสถานะ
- ทุกเอกสารต้องบอก fact/assumption/open question ให้ชัด
- เขียนให้ AI คนใหม่และเจ้าของที่ไม่เขียนโค้ดอ่านเข้าใจได้