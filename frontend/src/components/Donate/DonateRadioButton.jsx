import styles from '../../components/Donate/Donate.module.css';

const DonateRadioButton = ({ value, className, onChange, donateAmount }) => {
	const handeleRadio = () => {
		onChange(value)
	}
	return (
		<label htmlFor={value} className={styles.donate__formLabelRadio}>
			<input
				type="radio"
				name="donate"
				id={value}
				className={styles.donate__formRadio}
				onChange={handeleRadio}
				checked={value === +donateAmount}
			/>
			<span className={styles.donate__formDonation}>{value + '₽'}</span>
		</label>
	);
}
export default DonateRadioButton;