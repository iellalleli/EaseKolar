class SiblingNLS(db.Model):
    __tablename__ = 'siblings_nls'
    Applicant_ID = db.Column(db.String(20), db.ForeignKey('applicants.Applicant_ID'), nullable=False)
    SiblingNLS_ID = db.Column(db.String(20), primary_key=True)
    SbName_NLS = db.Column(db.String(40), nullable=False)
    SbAge_NLS = db.Column(db.Integer, nullable=False)
    SbCivilStatus_NLS = db.Column(db.String(1), nullable=False)
    SbHighestEducAttainment = db.Column(db.String(30), nullable=False)
    SbNatureOfWork = db.Column(db.String(2), nullable=False)
    SbCompany = db.Column(db.String(50), nullable=False)
    SbGrossAnnualIncome = db.Column(db.Numeric(10, 2), nullable=False)

    __table_args__ = (
        db.UniqueConstraint('Applicant_ID', 'SbName_NLS', 'SbAge_NLS', name='unique_sibling_nls'),
    )

    @staticmethod
    def generate_id():
        last_record = SiblingNLS.query.order_by(SiblingNLS.SiblingNLS_ID.desc()).first()
        if last_record:
            last_id = int(last_record.SiblingNLS_ID[3:])  # Skip the 'NLS' prefix
            new_id = f"NLS{last_id + 1:06d}"
        else:
            new_id = "NLS000001"
        return new_id
    
class SiblingSS(db.Model):
    __tablename__ = 'siblings_ss'
    Applicant_ID = db.Column(db.String(20), db.ForeignKey('applicants.Applicant_ID'), nullable=False)
    SiblingSS_ID = db.Column(db.String(20), primary_key=True)
    SbName_SS = db.Column(db.String(40), nullable=False)
    SbAge_SS = db.Column(db.Integer, nullable=False)
    SbCivilStatus_SS = db.Column(db.String(1), nullable=False)
    SbYearLevel = db.Column(db.String(30), nullable=False)
    SbSchoolName = db.Column(db.String(50), nullable=False)
    SbAnnualTuition = db.Column(db.Numeric(8, 2), nullable=True)
    SbTuitionPaidBy = db.Column(db.String(30), nullable=False)

    __table_args__ = (
        db.UniqueConstraint('Applicant_ID', 'SbName_SS', 'SbAge_SS', name='unique_sibling_ss'),
    )

    @staticmethod
    def generate_id():
        last_record = SiblingSS.query.order_by(SiblingSS.SiblingSS_ID.desc()).first()
        if last_record:
            last_id = int(last_record.SiblingSS_ID[2:])  # Skip the 'SS' prefix
            new_id = f"SS{last_id + 1:06d}"
        else:
            new_id = "SS000001"
        return new_id