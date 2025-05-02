-- SQL Server database schema setup for Auto Data Collector

CREATE TABLE Person (
    id INT IDENTITY(1,1) PRIMARY KEY,
    full_name NVARCHAR(255) NOT NULL,
    identity_card_number NVARCHAR(50) UNIQUE NOT NULL,
    date_of_birth DATE NOT NULL,
    birth_place NVARCHAR(255),
    height_cm FLOAT,
    weight_kg FLOAT,
    measurements NVARCHAR(50),
    body_art NVARCHAR(255),
    body_type NVARCHAR(50),
    butt_type NVARCHAR(50),
    breast_size NVARCHAR(50),
    level_of_education NVARCHAR(100),
    marital_status NVARCHAR(50),
    created_at DATETIME DEFAULT GETDATE(),
    updated_at DATETIME DEFAULT GETDATE()
);

-- Optional: Index for faster search
CREATE INDEX idx_identity_card ON Person (identity_card_number);
