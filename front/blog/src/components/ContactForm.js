


const ContactForm = () => (
    <>
        <form>
            <div className="mb-3">
                <input type="text" name="name" className="form-control" placeholder="Enter Name ..." required />
            </div>
            <div className="mb-3">
                <input type="email" name="email" className="form-control" placeholder="Enter Email ..." required />
            </div>
            <div className="mb-3">
                <textarea className="form-control" placeholder="description" name="description" required></textarea>
            </div>
            <button className="btn btn-success">
                Submit Form
            </button>
        </form>
    </>
)


export default ContactForm