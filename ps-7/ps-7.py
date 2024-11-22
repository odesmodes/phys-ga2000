G = 6.674e-11
M_earth = 5.974e24
m_moon = 7.348e22
R_earth_moon = 3.844e8 
M_sun = 1.989e30 
m_earth = 5.974e24 
m_jupiter = 1.898e27

m_prime_earth_moon = m_moon / M_earth
m_prime_earth_sun = m_earth / M_sun
m_prime_jupiter_sun = m_jupiter / M_sun

def f(r_prime, m_prime):
    return (1 / r_prime**2) - (m_prime / (1 - r_prime)**2) - r_prime

def f_prime(r_prime, m_prime):
    return -2 / r_prime**3 - 2 * m_prime / (1 - r_prime)**3 - 1

def solve_l1_point(m_prime, r_initial_guess, tolerance=1e-10, max_iterations=1000):
    r = r_initial_guess
    for iteration in range(max_iterations):
        f_val = f(r, m_prime)
        f_prime_val = f_prime(r, m_prime)
        
        if f_prime_val == 0:
            print("Derivative is zero. No solution found.")
            return None
        
        r_next = r - f_val / f_prime_val
        
        if abs(r_next - r) < tolerance:
            return r_next
        
        r = r_next
    
    print("Maximum iterations reached. No solution found.")
    return None

r_initial_guess_earth_moon = 0.2
r_initial_guess_earth_sun = 0.01
r_initial_guess_jupiter_sun = 0.05

r_prime_earth_moon = solve_l1_point(m_prime_earth_moon, r_initial_guess_earth_moon)
r_prime_earth_sun = solve_l1_point(m_prime_earth_sun, r_initial_guess_earth_sun)
r_prime_jupiter_sun = solve_l1_point(m_prime_jupiter_sun, r_initial_guess_jupiter_sun)

print(f"Earth-Moon system L1 point (r'): {r_prime_earth_moon}")
print(f"Earth-Sun system L1 point (r'): {r_prime_earth_sun}")
print(f"Jupiter-Sun system L1 point (r'): {r_prime_jupiter_sun}")
