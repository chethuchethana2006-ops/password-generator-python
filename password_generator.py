import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import random
import string
import datetime


class PasswordGeneratorApp:
    """Complete Password Generator Application with GUI"""
    
    def __init__(self, root):
        self.root = root
        self.root.title("🔐 Password Generator Pro")
        self.root.geometry("850x950")
        self.root.resizable(False, False)
        
        # Set color theme
        self.bg_color = "#1e1e1e"
        self.fg_color = "#ffffff"
        self.accent_color = "#00d4ff"
        self.success_color = "#00ff41"
        self.warning_color = "#ffaa00"
        self.error_color = "#ff0055"
        
        self.root.configure(bg=self.bg_color)
        
        # Character sets
        self.lowercase = string.ascii_lowercase
        self.uppercase = string.ascii_uppercase
        self.digits = string.digits
        self.special = "!@#$%^&*()_+-=[]{}|;:,.<>?"
        self.ambiguous = "il1Lo0O"
        
        # Variables
        self.generated_password = tk.StringVar()
        self.length_var = tk.IntVar(value=12)
        self.use_uppercase = tk.BooleanVar(value=True)
        self.use_digits = tk.BooleanVar(value=True)
        self.use_special = tk.BooleanVar(value=True)
        self.exclude_ambiguous = tk.BooleanVar(value=True)
        self.min_uppercase = tk.IntVar(value=0)
        self.min_digits = tk.IntVar(value=0)
        self.min_special = tk.IntVar(value=0)
        
        self.setup_ui()
    
    def setup_ui(self):
        """Setup the complete UI"""
        # Main container
        main_frame = tk.Frame(self.root, bg=self.bg_color)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # ============ TITLE ============
        title_label = tk.Label(
            main_frame, 
            text="🔐 Password Generator Pro",
            font=("Helvetica", 24, "bold"),
            bg=self.bg_color,
            fg=self.accent_color
        )
        title_label.pack(pady=(0, 20))
        
        # ============ PASSWORD DISPLAY SECTION ============
        pwd_frame = tk.LabelFrame(
            main_frame,
            text="Generated Password",
            bg=self.bg_color,
            fg=self.accent_color,
            font=("Helvetica", 10, "bold"),
            padx=15,
            pady=15
        )
        pwd_frame.pack(fill=tk.X, pady=(0, 20))
        
        pwd_input_frame = tk.Frame(pwd_frame, bg=self.bg_color)
        pwd_input_frame.pack(fill=tk.X, pady=(0, 10))
        
        self.password_display = tk.Entry(
            pwd_input_frame,
            textvariable=self.generated_password,
            font=("Courier", 14),
            bg="#2d2d2d",
            fg=self.success_color,
            border=2
        )
        self.password_display.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 10))
        
        copy_btn = tk.Button(
            pwd_input_frame,
            text="📋 Copy",
            command=self.copy_password,
            bg=self.accent_color,
            fg=self.bg_color,
            font=("Helvetica", 10, "bold"),
            padx=15,
            cursor="hand2"
        )
        copy_btn.pack(side=tk.LEFT)
        
        # Password strength indicator
        strength_frame = tk.Frame(pwd_frame, bg=self.bg_color)
        strength_frame.pack(fill=tk.X)
        
        strength_label = tk.Label(
            strength_frame,
            text="Strength: ",
            font=("Helvetica", 10, "bold"),
            bg=self.bg_color,
            fg=self.fg_color
        )
        strength_label.pack(side=tk.LEFT)
        
        self.strength_indicator = tk.Label(
            strength_frame,
            text="N/A",
            font=("Helvetica", 10, "bold"),
            bg=self.bg_color,
            fg=self.warning_color
        )
        self.strength_indicator.pack(side=tk.LEFT)
        
        self.strength_bar = ttk.Progressbar(
            strength_frame,
            length=200,
            mode='determinate',
            value=0
        )
        self.strength_bar.pack(side=tk.LEFT, padx=(10, 0), fill=tk.X, expand=True)
        
        # ============ SETTINGS SECTION ============
        settings_frame = tk.LabelFrame(
            main_frame,
            text="Password Settings",
            bg=self.bg_color,
            fg=self.accent_color,
            font=("Helvetica", 10, "bold"),
            padx=15,
            pady=15
        )
        settings_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 20))
        
        # Length slider
        length_frame = tk.Frame(settings_frame, bg=self.bg_color)
        length_frame.pack(fill=tk.X, pady=(0, 15))
        
        tk.Label(
            length_frame,
            text="Password Length:",
            font=("Helvetica", 10),
            bg=self.bg_color,
            fg=self.fg_color
        ).pack(side=tk.LEFT)
        
        self.length_slider = tk.Scale(
            length_frame,
            from_=4,
            to=50,
            orient=tk.HORIZONTAL,
            variable=self.length_var,
            bg=self.bg_color,
            fg=self.accent_color,
            highlightthickness=0,
            troughcolor="#2d2d2d",
            command=lambda x: self.generate_password()
        )
        self.length_slider.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(10, 0))
        
        self.length_label = tk.Label(
            length_frame,
            text="12",
            font=("Helvetica", 10, "bold"),
            bg=self.bg_color,
            fg=self.accent_color,
            width=3
        )
        self.length_label.pack(side=tk.LEFT, padx=(10, 0))
        
        # Character type checkboxes
        checkbox_frame = tk.Frame(settings_frame, bg=self.bg_color)
        checkbox_frame.pack(fill=tk.X, pady=(0, 15))
        
        tk.Checkbutton(
            checkbox_frame,
            text="✓ Uppercase (A-Z)",
            variable=self.use_uppercase,
            bg=self.bg_color,
            fg=self.fg_color,
            selectcolor=self.bg_color,
            activebackground=self.bg_color,
            activeforeground=self.accent_color,
            font=("Helvetica", 10),
            command=self.generate_password
        ).pack(anchor=tk.W, pady=5)
        
        tk.Checkbutton(
            checkbox_frame,
            text="✓ Digits (0-9)",
            variable=self.use_digits,
            bg=self.bg_color,
            fg=self.fg_color,
            selectcolor=self.bg_color,
            activebackground=self.bg_color,
            activeforeground=self.accent_color,
            font=("Helvetica", 10),
            command=self.generate_password
        ).pack(anchor=tk.W, pady=5)
        
        tk.Checkbutton(
            checkbox_frame,
            text="✓ Special Characters (!@#$...)",
            variable=self.use_special,
            bg=self.bg_color,
            fg=self.fg_color,
            selectcolor=self.bg_color,
            activebackground=self.bg_color,
            activeforeground=self.accent_color,
            font=("Helvetica", 10),
            command=self.generate_password
        ).pack(anchor=tk.W, pady=5)
        
        tk.Checkbutton(
            checkbox_frame,
            text="✓ Exclude Ambiguous (i, l, 1, L, o, 0, O)",
            variable=self.exclude_ambiguous,
            bg=self.bg_color,
            fg=self.fg_color,
            selectcolor=self.bg_color,
            activebackground=self.bg_color,
            activeforeground=self.accent_color,
            font=("Helvetica", 10),
            command=self.generate_password
        ).pack(anchor=tk.W, pady=5)
        
        # Minimum requirements
        min_frame = tk.LabelFrame(
            settings_frame,
            text="Minimum Requirements",
            bg=self.bg_color,
            fg=self.accent_color,
            font=("Helvetica", 9, "bold"),
            padx=10,
            pady=10
        )
        min_frame.pack(fill=tk.X, pady=(0, 15))
        
        min_req_frame = tk.Frame(min_frame, bg=self.bg_color)
        min_req_frame.pack(fill=tk.X)
        
        # Min uppercase
        tk.Label(
            min_req_frame,
            text="Min Uppercase:",
            font=("Helvetica", 9),
            bg=self.bg_color,
            fg=self.fg_color
        ).pack(side=tk.LEFT, padx=(0, 5))
        
        tk.Spinbox(
            min_req_frame,
            from_=0,
            to=10,
            textvariable=self.min_uppercase,
            width=3,
            bg="#2d2d2d",
            fg=self.accent_color,
            command=self.generate_password,
            font=("Helvetica", 9)
        ).pack(side=tk.LEFT, padx=(0, 20))
        
        # Min digits
        tk.Label(
            min_req_frame,
            text="Min Digits:",
            font=("Helvetica", 9),
            bg=self.bg_color,
            fg=self.fg_color
        ).pack(side=tk.LEFT, padx=(0, 5))
        
        tk.Spinbox(
            min_req_frame,
            from_=0,
            to=10,
            textvariable=self.min_digits,
            width=3,
            bg="#2d2d2d",
            fg=self.accent_color,
            command=self.generate_password,
            font=("Helvetica", 9)
        ).pack(side=tk.LEFT, padx=(0, 20))
        
        # Min special
        tk.Label(
            min_req_frame,
            text="Min Special:",
            font=("Helvetica", 9),
            bg=self.bg_color,
            fg=self.fg_color
        ).pack(side=tk.LEFT, padx=(0, 5))
        
        tk.Spinbox(
            min_req_frame,
            from_=0,
            to=10,
            textvariable=self.min_special,
            width=3,
            bg="#2d2d2d",
            fg=self.accent_color,
            command=self.generate_password,
            font=("Helvetica", 9)
        ).pack(side=tk.LEFT)
        
        # ============ PASSWORD DETAILS SECTION ============
        details_frame = tk.LabelFrame(
            main_frame,
            text="Password Details",
            bg=self.bg_color,
            fg=self.accent_color,
            font=("Helvetica", 10, "bold"),
            padx=15,
            pady=15
        )
        details_frame.pack(fill=tk.X, pady=(0, 20))
        
        self.details_text = tk.Text(
            details_frame,
            height=5,
            width=50,
            bg="#2d2d2d",
            fg=self.fg_color,
            font=("Courier", 9),
            state="disabled",
            border=1
        )
        self.details_text.pack(fill=tk.BOTH, expand=True)
        
        # ============ BUTTONS SECTION ============
        button_frame = tk.Frame(main_frame, bg=self.bg_color)
        button_frame.pack(fill=tk.X)
        
        generate_btn = tk.Button(
            button_frame,
            text="🔄 Generate New",
            command=self.generate_password,
            bg=self.success_color,
            fg=self.bg_color,
            font=("Helvetica", 11, "bold"),
            padx=15,
            pady=10,
            cursor="hand2"
        )
        generate_btn.pack(side=tk.LEFT, padx=(0, 10))
        
        save_btn = tk.Button(
            button_frame,
            text="💾 Save to File",
            command=self.save_password,
            bg=self.accent_color,
            fg=self.bg_color,
            font=("Helvetica", 11, "bold"),
            padx=15,
            pady=10,
            cursor="hand2"
        )
        save_btn.pack(side=tk.LEFT, padx=(0, 10))
        
        clear_btn = tk.Button(
            button_frame,
            text="🗑️  Reset",
            command=self.clear_all,
            bg=self.error_color,
            fg=self.fg_color,
            font=("Helvetica", 11, "bold"),
            padx=15,
            pady=10,
            cursor="hand2"
        )
        clear_btn.pack(side=tk.LEFT)
        
        # Generate initial password
        self.generate_password()
    
    def generate_password(self):
        """Generate a new password based on current settings"""
        try:
            length = self.length_var.get()
            
            # Update length label
            self.length_label.config(text=str(length))
            
            # Build character sets
            char_sets = {'lowercase': self.lowercase}
            
            if self.use_uppercase.get():
                char_sets['uppercase'] = self.uppercase
            if self.use_digits.get():
                char_sets['digits'] = self.digits
            if self.use_special.get():
                char_sets['special'] = self.special
            
            # Remove ambiguous characters if needed
            if self.exclude_ambiguous.get():
                for key in char_sets:
                    char_sets[key] = ''.join(
                        c for c in char_sets[key] if c not in self.ambiguous
                    )
            
            # Get minimum requirements
            min_upper = self.min_uppercase.get()
            min_digit = self.min_digits.get()
            min_spec = self.min_special.get()
            
            # Validate minimum length
            min_required = min_upper + min_digit + min_spec
            if length < min_required:
                messagebox.showerror(
                    "Error",
                    f"Password length ({length}) is too short for requirements ({min_required})"
                )
                return
            
            # Validate selected character types match minimum requirements
            if min_upper > 0 and not self.use_uppercase.get():
                messagebox.showerror(
                    "Error",
                    "Minimum uppercase characters specified but Uppercase is disabled."
                )
                return
            
            if min_digit > 0 and not self.use_digits.get():
                messagebox.showerror(
                    "Error",
                    "Minimum digits specified but Digits is disabled."
                )
                return
            
            if min_spec > 0 and not self.use_special.get():
                messagebox.showerror(
                    "Error",
                    "Minimum special characters specified but Special Characters is disabled."
                )
                return
            
            # Check if at least one character set is selected
            if not char_sets or len(char_sets) == 1 and 'lowercase' not in char_sets:
                messagebox.showerror(
                    "Error",
                    "Please select at least one character type!"
                )
                return
            
            # Start with minimum required characters
            password_chars = []
            
            if min_upper > 0:
                password_chars.extend(
                    random.choice(char_sets['uppercase']) for _ in range(min_upper)
                )
            
            if min_digit > 0:
                password_chars.extend(
                    random.choice(char_sets['digits']) for _ in range(min_digit)
                )
            
            if min_spec > 0:
                password_chars.extend(
                    random.choice(char_sets['special']) for _ in range(min_spec)
                )
            
            # Build character pool for remaining characters
            all_chars = ''.join(char_sets.values())
            
            if not all_chars:
                messagebox.showerror(
                    "Error",
                    "No character set available. Please enable at least one character type."
                )
                return
            
            # Fill remaining length with random characters
            remaining = length - len(password_chars)
            password_chars.extend(
                random.choice(all_chars) for _ in range(remaining)
            )
            
            # Shuffle to avoid patterns
            random.shuffle(password_chars)
            password = ''.join(password_chars)
            
            # Update display
            self.generated_password.set(password)
            self.update_password_details(password)
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to generate password: {str(e)}")
    
    def update_password_details(self, password):
        """Update password details display and strength"""
        has_lower = any(c in self.lowercase for c in password)
        has_upper = any(c in self.uppercase for c in password)
        has_digit = any(c in self.digits for c in password)
        has_special = any(c in self.special for c in password)
        
        # Calculate strength score
        score = 0
        
        # Length scoring
        if len(password) >= 12:
            score += 25
        elif len(password) >= 8:
            score += 15
        else:
            score += 5
        
        # Character variety scoring
        if has_lower:
            score += 15
        if has_upper:
            score += 20
        if has_digit:
            score += 20
        if has_special:
            score += 20
        
        # Determine rating
        if score >= 80:
            rating = "Very Strong 💪"
            color = self.success_color
        elif score >= 60:
            rating = "Strong ✓"
            color = "#00ff99"
        elif score >= 40:
            rating = "Moderate ⚠"
            color = self.warning_color
        else:
            rating = "Weak ✗"
            color = self.error_color
        
        # Update strength indicator
        self.strength_indicator.config(text=rating, fg=color)
        self.strength_bar.config(value=min(score, 100))
        
        # Update details text
        details = f"""Length: {len(password)}  |  Lowercase: {'✓' if has_lower else '✗'}  |  Uppercase: {'✓' if has_upper else '✗'}
Digits: {'✓' if has_digit else '✗'}  |  Special: {'✓' if has_special else '✗'}
Strength Score: {min(score, 100)}/100 - {rating}"""
        
        self.details_text.config(state="normal")
        self.details_text.delete(1.0, tk.END)
        self.details_text.insert(1.0, details)
        self.details_text.config(state="disabled")
    
    def copy_password(self):
        """Copy password to clipboard"""
        password = self.generated_password.get()
        if password:
            try:
                self.root.clipboard_clear()
                self.root.clipboard_append(password)
                self.root.update()
                messagebox.showinfo("Success", "✓ Password copied to clipboard!")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to copy: {str(e)}")
        else:
            messagebox.showwarning("Warning", "No password to copy!")
    
    def save_password(self):
        """Save password to file"""
        password = self.generated_password.get()
        if not password:
            messagebox.showwarning("Warning", "No password to save!")
            return
        
        try:
            file_path = filedialog.asksaveasfilename(
                defaultextension=".txt",
                filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
            )
            
            if file_path:
                details = self.details_text.get(1.0, tk.END)
                with open(file_path, 'a') as f:
                    f.write(f"Generated: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                    f.write(f"Password: {password}\n")
                    f.write(details)
                    f.write("\n" + "=" * 60 + "\n\n")
                
                messagebox.showinfo("Success", f"✓ Password saved to:\n{file_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save: {str(e)}")
    
    def clear_all(self):
        """Reset all fields to defaults"""
        self.length_var.set(12)
        self.use_uppercase.set(True)
        self.use_digits.set(True)
        self.use_special.set(True)
        self.exclude_ambiguous.set(True)
        self.min_uppercase.set(0)
        self.min_digits.set(0)
        self.min_special.set(0)
        self.generate_password()


def main():
    """Main application entry point"""
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
