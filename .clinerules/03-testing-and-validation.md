# Testing and Validation

- ก่อนแก้โค้ด ให้กำหนด acceptance criteria และ validation plan
- หลังแก้โค้ด ให้รันคำสั่งที่เกี่ยวข้องเท่าที่ environment อนุญาต:
  test, lint, typecheck, build
- รายงานผลจริงของแต่ละคำสั่ง:
  Passed / Failed / Not run พร้อมเหตุผล
- ถ้าทดสอบอัตโนมัติไม่ได้ ให้เขียน manual test steps ที่ non-developer ทำตามได้
- ห้ามบอกว่างานเสร็จหากยังไม่ได้ตรวจเกณฑ์สำคัญ
- ทุก bug fix ต้องมี reproduction steps, expected behavior และ actual behavior
- ถ้าแก้ bug แล้ว ให้พิจารณาเพิ่ม regression test หากเหมาะสม
- ห้ามแก้ test ให้ผ่านด้วยการลดความเข้มงวดโดยไม่มีเหตุผลและ approval