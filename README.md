# Notched-Beam-Flexural-Testing-Steel-Fiber-Reinforced-Concrete
# Introduction
Steel fiber reinforced concrete (SFRC) is increasingly adopted in structural applications due to its enhanced tensile behaviour and improved ductility after cracking. This test investigates the flexural performance of SFRC beams through a three-point bending test, simulating a crack mouth opening scenario. The test protocol is designed in accordance with the RILEM TC 162‐TDF recommendations, which specify limitations such as maximum steel fiber length (≤ 60 mm) and aggregate size (< 32 mm) to ensure homogeneous distribution and consistent performance. A critical aspect of this test is the use of a very low displacement rate (0.22 mm/min) that ensures quasi-static loading, thereby minimizing dynamic stress wave oscillations and inertial effects. Moreover, the linear relationship between midspan deflection (δ) and CMOD, typically expressed as:  

![image](https://github.com/user-attachments/assets/9de62a48-e5bd-4547-b393-aaa9ccba2e98)


provides a means to correlate global deflection with local crack opening behaviour in the post-peak regime.  

## 2. Materials and Methods

### 2.1 Specimen Geometry and Preparation

**Dimensions:**  
- Overall: 500 mm (length) × 100 mm (width) × 100 mm (depth).  
- Notch: A 10 mm deep notch is introduced at midspan, reducing the effective depth (hsp) to 90 mm.  
- Clear Span: The supports are spaced 450 mm apart.  

**Material Constraints:**  
- Aggregate size is maintained below 32 mm.  
- Steel fibers do not exceed 60 mm in length to comply with the standard.  

**Casting:**  
- Specimens were cast using a controlled mixing procedure to ensure even fiber dispersion.  

### 2.2 Test Setup and Instrumentation

**Loading Configuration:**  
- Three-point bending test with a centrally applied single point load.  

**Displacement Control:**  
- The load is applied at a constant rate of 0.22 mm/min. This low rate ensures quasi-static conditions, thereby eliminating the potential for dynamic effects that could introduce errors in deflection and CMOD measurements.  

**Measurement Devices:**  
- **Load Cell:** Accuracy of 0.1 kN.  
- **CMOD Gauge:** Installed at the notch with similar precision, ensuring accurate capture of crack propagation.  

**Data Acquisition:**  
- During the first two minutes, data is logged at 5 Hz, then at 1 Hz for the remainder of the test.  

## 3. Test Procedure and Calculations

### 3.1 Experimental Procedure

**Specimen Preparation and Notching:**  
- After demoulding (within 24–48 hours), beams are cured and then notched using a wet sawing process. The notch is sawn at midspan along the beam’s width, with the sawing width limited to 5 mm.  

**Testing Configuration:**  
- The beam is positioned on roller supports with a 450 mm clear span.  
- The load is applied at midspan, and the displacement (δ) is recorded continuously.  

**Data Recording:**  
- Force, deflection, and CMOD are continuously logged. Initial data is captured at high frequency to ensure an accurate representation of the elastic response.  

### 3.2 Calculation of Key Parameters

#### 3.2.1 Limit of Proportionality (LOP)  

The limit of proportionality load \(F_L\) is identified as the maximum load recorded within a narrow deflection interval (typically around \( \delta = 0.05 \) mm). The corresponding midspan moment is calculated by:

![image](https://github.com/user-attachments/assets/4f0c9396-4ebd-45f7-95ac-5c3e1a3833a5)


where \(L\) is the clear span (450 mm).  

#### 3.2.2 Equivalent Flexural Tensile Strength  

Assuming a stress distribution as in Fig. 7 of the RILEM [1] guideline, the equivalent flexural tensile strength \( f_{eq} \) is given by:

![image](https://github.com/user-attachments/assets/0dcc7276-372a-46c7-a362-4b82a5d64d2b)

where \( b \) is the width (100 mm) and \( h_{sp} \) is the effective depth (90 mm).  

#### 3.2.3 Energy Absorption (Flexural Energy)  

The flexural energy is determined by calculating the area under the load–deflection curve up to a prescribed deflection \( \delta_i \). This area can be divided into two contributions:  

- **Concrete Contribution (DBZ)**  
- **Steel Fiber Contribution (Df)**  

Mathematically, the total energy absorbed \( D_{total} \) is given by:

![image](https://github.com/user-attachments/assets/9f40b0c7-7219-422b-af36-c30cb8217a9c)


where \( F(\delta) \) is the load as a function of deflection.  

#### 3.2.4 CMOD–δ Relationship  

The established linear correlation in the post-peak region is:

![image](https://github.com/user-attachments/assets/4ecf5a73-fe02-40a6-a5a5-b89d1d6a9a60)


which facilitates conversion between global deflection and local crack opening displacement.  
