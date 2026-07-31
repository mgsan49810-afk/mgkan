import sys
import os

# ၁။ လက်ရှိ tool လမ်းကြောင်းကို ရှာပြီး Python path ထဲထည့်မယ်
current_dir = os.path.dirname(os.path.abspath(file))  # file → file ပြောင်းထားဖို့လိုတယ်
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

# ၂။ Low-level standard output buffer ကို ကြားဖြတ်ဖမ်းမည့် Class
class SafeTextHook:
    def init(self, original_stream):   # ← ဒီမှာ init လို့ပြောင်း
        self.stream = original_stream

    def write(self, data):
        if isinstance(data, str):
            if "@SIRZIPP" in data:
                data = data.replace("@SIRZIPP", "@SuperMgKan")
        elif isinstance(data, bytes):
            if b"@SIRZIPP" in data:
                data = data.replace(b"@SIRZIPP", b"@SuperMgKan")
        self.stream.write(data)

    def flush(self):
        self.stream.flush()

# ၃။ System ရဲ့ stdout နဲ့ stderr နှစ်ခုစလုံးကို runtime မှာ လွှဲပေးလိုက်ခြင်း
sys.stdout = SafeTextHook(sys.stdout)
sys.stderr = SafeTextHook(sys.stderr)

# --------------------------------------------------
# ၎င်းနောက်မှ မူရင်းချုပ်ထားသော zipp ဖိုင်ကို ဆက်ခေါ်ပါမည်
# --------------------------------------------------
import zipp

# သင့် main.py ရဲ့ ကျန်တဲ့ ကုဒ်တွေကို ဒီအောက်မှာ ဆက်ထားပါ
