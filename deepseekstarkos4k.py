import tkinter as tk
from tkinter import scrolledtext, messagebox, ttk, simpledialog
import platform
import subprocess
import time
import random
import math
import os
import sys
import io
import contextlib
import ctypes

# =========================================================
# ALGORITHM: C.A.T. In-Memory Virtual File System (VFS)
# =========================================================
class CATVFS:
    """A high-performance in-memory hierarchical file management system."""
    def __init__(self):
        # Initial memory state tree - branded for Stark OS with C.A.T.
        self.memory_tree = {
            "ROOT:": {
                "System": {
                    "kernel.stark": "HEX_0x7FFA_STARK_CORE_v2.0",
                    "ui_config.json": "{\"theme\": \"Arc_Reactor\", \"access\": \"Level_7\"}"
                },
                "Neural_Links": {
                    "Tony": {
                        "mission_log.txt": "Stark OS 2.0 online.\nC.A.T., suit up.",
                    },
                    "Archive": {}
                }
            }
        }

    def _traverse(self, path):
        parts = [p for p in path.split("/") if p and p != "ROOT:"]
        current_node = self.memory_tree["ROOT:"]
        for part in parts:
            if part in current_node and isinstance(current_node, dict):
                current_node = current_node[part]
            else:
                return None
        return current_node

    def list_contents(self, path):
        node = self._traverse(path)
        return list(node.keys()) if isinstance(node, dict) else []

    def is_directory(self, path, name):
        node = self._traverse(path)
        if isinstance(node, dict) and name in node:
            return isinstance(node[name], dict)
        return False

    def write_file(self, path, filename, content):
        node = self._traverse(path)
        if isinstance(node, dict):
            if filename not in node or not isinstance(node[filename], dict):
                node[filename] = content
                return True
        return False

    def read_file(self, path, filename):
        node = self._traverse(path)
        if isinstance(node, dict) and filename in node:
            if not isinstance(node[filename], dict):
                return node[filename]
        return None

    def delete_item(self, path, name):
        node = self._traverse(path)
        if isinstance(node, dict) and name in node:
            del node[name]
            return True
        return False

# =========================================================
# CORE OS ENGINE: Stark OS 2.0 (MCU Interface with C.A.T.)
# =========================================================
class StarkOS:
    def __init__(self, root):
        self.root = root
        self.root.title("STARK OS v2.0 // C.A.T. HOLOGRAPHIC INTERFACE")
        
        # Force true fullscreen for maximum immersion
        self.root.attributes("-fullscreen", True)
        self.root.geometry("1920x1080")
        self.root.resizable(False, False)
        
        # Allow exiting fullscreen with the Escape key
        self.root.bind("<Escape>", lambda e: self.root.attributes("-fullscreen", False))
        
        # Stark Industries HUD Color Palette (MCU style)
        self.bg_deep = "#0a0f1a"      # Deep Space
        self.bg_panel = "#1a1f2e"     # Panel Dark
        self.cyan = "#4fc3ff"         # Arc Reactor Blue
        self.indigo = "#7e9eff"       # HUD Indigo
        self.pink = "#ff7eb3"         # Alert Pink
        self.gold = "#ffd966"         # Stark Gold
        self.text_dim = "#a0b0c0"     # Ghost Text
        
        self.root.configure(bg="black")
        self.host_os = platform.system()
        self.vfs = CATVFS() 
        
        self.init_boot_sequence()

    def init_boot_sequence(self):
        """MCU-style boot sequence simulation with C.A.T. AI."""
        self.boot_frame = tk.Frame(self.root, bg="black")
        self.boot_frame.pack(fill=tk.BOTH, expand=True)

        # Scaled up font size for 1080p
        self.boot_log = tk.Text(self.boot_frame, bg="black", fg=self.cyan, 
                                font=("Consolas", 16), bd=0, highlightthickness=0)
        self.boot_log.pack(fill=tk.BOTH, expand=True, padx=80, pady=80)

        steps = [
            (">> INITIALIZING STARK OS 2.0 [ARC REACTOR CORE]", 400),
            (">> C.A.T. (Central Advanced Technician): Good morning, Tony.", 300),
            (">> SCANNING HARDWARE TOPOLOGY...", 300),
            (f">> DETECTED HOST: {self.host_os.upper()} // SUIT COMPATIBILITY: 98%", 200),
            (">> ESTABLISHING NEURAL LINK...", 600),
            (">> [OK] SYNCING MEMORY RECURSION...", 200),
            (">> [OK] MOUNTING VFS (RAM_ONLY)...", 300),
            (">> [OK] DEPLOYING HOLOGRAPHIC OVERLAY...", 400),
            (">> SYSTEM READY. SUIT STATUS: NOMINAL. WELCOME, TONY.", 800)
        ]

        def process_boot(idx):
            if idx < len(steps):
                msg, delay = steps[idx]
                self.boot_log.insert(tk.END, msg + "\n")
                self.boot_log.see(tk.END)
                self.root.after(delay, lambda: process_boot(idx + 1))
            else:
                self.root.after(500, self.launch_desktop)

        process_boot(0)

    def launch_desktop(self):
        self.boot_frame.destroy()
        self.root.configure(bg=self.bg_deep)
        
        # Draw HUD Canvas at 1920x1080
        self.canvas = tk.Canvas(self.root, bg=self.bg_deep, highlightthickness=0)
        self.canvas.place(x=0, y=0, width=1920, height=1080)
        self.draw_hud_decorations()
        
        # Start Arc Reactor animation
        self.angle = 0
        self.animate_arc_reactor()

        self.setup_ui_layers()

    def draw_hud_decorations(self):
        # Top Header Bar - updated to span 1920px width
        self.canvas.create_rectangle(0, 0, 1920, 60, fill=self.bg_panel, outline=self.cyan)
        self.canvas.create_text(40, 30, text="STARK OS 2.0 // C.A.T. ONLINE // SYSTEM STATUS: NOMINAL", 
                                fill=self.cyan, font=("Consolas", 18, "bold"), anchor="w")
        
        # Bottom Taskbar Area - adjusted for 1080 height
        self.canvas.create_rectangle(0, 1020, 1920, 1080, fill=self.bg_panel, outline=self.cyan)
        
        # Decorative HUD Corners - Top Left
        self.canvas.create_line(30, 80, 100, 80, fill=self.cyan, width=4)
        self.canvas.create_line(30, 80, 30, 150, fill=self.cyan, width=4)
        
        # Decorative HUD Corners - Top Right
        self.canvas.create_line(1820, 80, 1890, 80, fill=self.cyan, width=4)
        self.canvas.create_line(1890, 80, 1890, 150, fill=self.cyan, width=4)

        # Arc Reactor circle (centered horizontally at 960)
        self.arc_reactor = self.canvas.create_oval(910, 30, 1010, 130, outline=self.cyan, width=2)

    def animate_arc_reactor(self):
        # Simple rotating effect
        self.angle += 5
        x0, y0, x1, y1 = 910, 30, 1010, 130
        cx = (x0 + x1) / 2
        cy = (y0 + y1) / 2
        r = 50
        # Draw two rotating arcs
        self.canvas.delete("arc")
        self.canvas.create_arc(cx-r, cy-r, cx+r, cy+r, start=self.angle, extent=120, 
                               outline=self.cyan, width=4, style="arc", tag="arc")
        self.canvas.create_arc(cx-r, cy-r, cx+r, cy+r, start=self.angle+180, extent=120, 
                               outline=self.gold, width=4, style="arc", tag="arc")
        self.root.after(50, self.animate_arc_reactor)

    def setup_ui_layers(self):
        # Centering the main container in the 1920x1080 space
        self.main_container = tk.Frame(self.root, bg=self.bg_deep)
        self.main_container.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # Icon Grid
        self.create_hud_icon("⚡\nARC_REACTOR", 0, 0, self.open_arc_reactor)
        self.create_hud_icon("📁\nVFS_CORE", 0, 1, self.open_vfs_explorer)
        self.create_hud_icon("🔧\nSUIT_COMPILER", 0, 2, self.open_compiler)
        self.create_hud_icon("🤖\nC.A.T.", 1, 0, self.open_cat_ai)
        self.create_hud_icon("🌐\nHOST_BRIDGE", 1, 1, self.open_host_bridge)
        self.create_hud_icon("💬\nTERMINAL", 1, 2, self.open_stark_terminal)
        
        # Clock - placed accurately inside the new bottom taskbar
        self.clock_lbl = tk.Label(self.root, text="", bg=self.bg_panel, fg=self.cyan, font=("Consolas", 16))
        self.clock_lbl.place(x=1750, y=1035)
        self.update_clock()

    def update_clock(self):
        self.clock_lbl.config(text=time.strftime("%H:%M:%S UTC"))
        self.root.after(1000, self.update_clock)

    def create_hud_icon(self, label, row, col, cmd):
        frame = tk.Frame(self.main_container, bg=self.bg_deep, bd=2, highlightbackground=self.indigo, highlightthickness=2)
        frame.grid(row=row, column=col, padx=30, pady=30)
        
        # Scaled up icons to fit the 1080p screen real estate
        btn = tk.Button(frame, text=label, bg=self.bg_panel, fg=self.cyan, 
                        font=("Consolas", 14, "bold"), relief=tk.FLAT, width=22, height=7,
                        activebackground=self.cyan, activeforeground="black", command=cmd)
        btn.pack()

    # ---------------------------------------------------------
    # FEATURE: ARC REACTOR CORE (was ASM Engine)
    # ---------------------------------------------------------
    def open_arc_reactor(self):
        win = self.create_hud_window("ARC REACTOR CORE", 800, 600)
        
        tk.Label(win, text="[ENERGY PULSE SIMULATION]", bg=self.bg_panel, fg=self.pink, font=("Consolas", 12)).pack(pady=10)
        
        code_in = scrolledtext.ScrolledText(win, bg="black", fg=self.cyan, font=("Consolas", 12), height=8)
        code_in.pack(fill=tk.X, padx=20, pady=10)
        code_in.insert(tk.END, "b8 2a 00 00 00 c3  # mov eax, 42; ret")

        log = scrolledtext.ScrolledText(win, bg="black", fg=self.text_dim, font=("Consolas", 11), height=12)
        log.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

        def run_pulse():
            hex_data = code_in.get("1.0", tk.END).split("#")[0].strip().replace(" ", "")
            log.insert(tk.END, f">> Allocating HUD buffer for {len(hex_data)//2} bytes...\n")
            try:
                shellcode = bytes.fromhex(hex_data)
                if platform.system() == "Windows":
                    kernel32 = ctypes.windll.kernel32
                    ptr = kernel32.VirtualAlloc(0, len(shellcode), 0x3000, 0x40)
                    buf = (ctypes.c_char * len(shellcode)).from_buffer_copy(shellcode)
                    kernel32.RtlMoveMemory(ptr, buf, len(shellcode))
                    res = ctypes.CFUNCTYPE(ctypes.c_int)(ptr)()
                    log.insert(tk.END, f">> EAX RESULT: {res}\n")
                else:
                    log.insert(tk.END, ">> OS Security level prevents direct ASM on non-Win host.\n")
            except Exception as e:
                log.insert(tk.END, f">> SEGFAULT: {e}\n")

        tk.Button(win, text="EXECUTE PULSE", font=("Consolas", 12, "bold"), bg=self.cyan, fg="black", command=run_pulse, height=2).pack(pady=10)

    # ---------------------------------------------------------
    # FEATURE: C.A.T. AI (was BYTEBOT)
    # ---------------------------------------------------------
    def open_cat_ai(self):
        win = self.create_hud_window("C.A.T. (Central Advanced Technician)", 900, 750)
        
        tk.Label(win, text="INPUT OBJECTIVE:", bg=self.bg_panel, fg=self.cyan, font=("Consolas", 12)).pack(anchor="w", padx=20, pady=(10,0))
        prompt = tk.Entry(win, bg="black", fg=self.cyan, insertbackground=self.cyan, font=("Consolas", 14))
        prompt.pack(fill=tk.X, padx=20, pady=10)
        prompt.insert(0, "Quick Sort Algorithm")

        code_view = scrolledtext.ScrolledText(win, bg="black", fg=self.indigo, font=("Consolas", 14), height=18)
        code_view.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

        def generate():
            p = prompt.get().lower()
            if "sort" in p:
                c = "def sort(a):\n  if len(a)<=1: return a\n  p=a[0]\n  return sort([x for x in a[1:] if x<p])+[p]+sort([x for x in a[1:] if x>=p])\n\ndata=[9,3,7,1,5]\nprint(f'Input: {data}')\nprint(f'Sorted: {sort(data)}')"
            elif "prime" in p:
                c = "def is_prime(n):\n  return n > 1 and all(n % i for i in range(2, int(n**0.5)+1))\n\nprint([x for x in range(50) if is_prime(x)])"
            else:
                c = "print('C.A.T.: Objective identified but no template match.')"
            
            code_view.delete("1.0", tk.END)
            code_view.insert(tk.END, c)

        def execute():
            src = code_view.get("1.0", tk.END)
            out = io.StringIO()
            try:
                with contextlib.redirect_stdout(out):
                    exec(compile(src, '<cat_ai>', 'exec'))
                messagebox.showinfo("Execution Results", out.getvalue())
            except Exception as e:
                messagebox.showerror("Runtime Error", str(e))

        btn_f = tk.Frame(win, bg=self.bg_panel)
        btn_f.pack(pady=15)
        tk.Button(btn_f, text="GENERATE", font=("Consolas", 12, "bold"), bg=self.indigo, fg="white", command=generate, width=15, height=2).pack(side="left", padx=10)
        tk.Button(btn_f, text="EXECUTE", font=("Consolas", 12, "bold"), bg=self.cyan, fg="black", command=execute, width=15, height=2).pack(side="left", padx=10)

    # ---------------------------------------------------------
    # UTILS: STARK WINDOW FACTORY
    # ---------------------------------------------------------
    def create_hud_window(self, title, w, h):
        win = tk.Toplevel(self.root)
        win.title(title)
        win.geometry(f"{w}x{h}")
        win.configure(bg=self.bg_panel)
        
        # Header Decor
        header = tk.Frame(win, bg=self.cyan, height=4)
        header.pack(fill=tk.X)
        
        title_lbl = tk.Label(win, text=f"// {title}", bg=self.bg_panel, fg=self.cyan, font=("Consolas", 14, "bold"))
        title_lbl.pack(pady=10)
        
        return win

    def open_vfs_explorer(self):
        win = self.create_hud_window("VFS EXPLORER", 600, 600)
        curr_path = tk.StringVar(value="/ROOT:")
        
        listbox = tk.Listbox(win, bg="black", fg=self.cyan, font=("Consolas", 14), bd=0)
        listbox.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        def refresh():
            listbox.delete(0, tk.END)
            for item in self.vfs.list_contents(curr_path.get()):
                p = "[DIR] " if self.vfs.is_directory(curr_path.get(), item) else "[FIL] "
                listbox.insert(tk.END, p + item)

        tk.Button(win, text="REFRESH PATH", font=("Consolas", 12, "bold"), command=refresh, bg=self.indigo, fg="white", height=2).pack(pady=10)
        refresh()

    def open_compiler(self):
        win = self.create_hud_window("SUIT COMPILER", 800, 600)
        code = scrolledtext.ScrolledText(win, bg="black", fg=self.gold, font=("Consolas", 14))
        code.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        code.insert(tk.END, "import math\n# Compute Fibonacci in RAM\nphi = (1 + math.sqrt(5)) / 2\n[int((phi**n - (-1/phi)**n) / math.sqrt(5)) for n in range(15)]")
        
        def run():
            try:
                res = eval(code.get("1.0", tk.END))
                messagebox.showinfo("Memory Dump", f"Output: {res}")
            except Exception as e:
                messagebox.showerror("Error", str(e))
        
        tk.Button(win, text="COMPILE & EVAL", font=("Consolas", 12, "bold"), command=run, bg=self.cyan, fg="black", height=2).pack(pady=10)

    def open_host_bridge(self):
        win = self.create_hud_window("HOST BRIDGE", 450, 350)
        tk.Label(win, text=f"INTERFACE: {self.host_os}", bg=self.bg_panel, fg=self.text_dim, font=("Consolas", 12)).pack(pady=20)
        
        def launch(name):
            try:
                if self.host_os == "Windows": subprocess.Popen(f"{name}.exe")
                else: messagebox.showwarning("Bridge", "Host bridge optimized for x64 Windows.")
            except: pass

        tk.Button(win, text="OS_CALC", font=("Consolas", 12, "bold"), width=20, height=2, command=lambda: launch("calc")).pack(pady=10)
        tk.Button(win, text="OS_TERM", font=("Consolas", 12, "bold"), width=20, height=2, command=lambda: launch("cmd")).pack(pady=10)

    def open_stark_terminal(self):
        win = self.create_hud_window("STARK TERMINAL", 800, 600)
        term = scrolledtext.ScrolledText(win, bg="black", fg=self.cyan, font=("Consolas", 14), insertbackground=self.cyan)
        term.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        term.insert(tk.END, "STARK OS 2.0 // C.A.T. SHELL\n>> ")

        def on_enter(e):
            lines = term.get("1.0", tk.END).split("\n")
            cmd = lines[-2].replace(">> ", "").strip()
            if cmd == "help": term.insert(tk.END, "Commands: clear, sys, vfs, exit\n")
            elif cmd == "sys": term.insert(tk.END, f"STARK_CORE_v2.0 // C.A.T. ACTIVE // {self.host_os}\n")
            elif cmd == "vfs": term.insert(tk.END, f"VFS mounted: {list(self.vfs.memory_tree.keys())}\n")
            elif cmd == "clear": term.delete("1.0", tk.END)
            elif cmd == "exit": self.root.destroy()
            term.insert(tk.END, ">> ")
            term.see(tk.END)
            return "break"

        term.bind("<Return>", on_enter)

if __name__ == "__main__":
    root = tk.Tk()
    # Removed DPI awareness override so Windows automatically scales 
    # the 1080p window up to fit properly on 1440p or 4K monitors.
    app = StarkOS(root)
    root.mainloop()
