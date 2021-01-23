// Code generated by go-swagger; DO NOT EDIT.

package memberships

// This file was generated by the swagger tool.
// Editing this file might prove futile when you re-run the swagger generate command

import (
	"context"
	"net/http"
	"time"

	"github.com/go-openapi/errors"
	"github.com/go-openapi/runtime"
	cr "github.com/go-openapi/runtime/client"
	"github.com/go-openapi/strfmt"
)

// NewDeleteMembershipParams creates a new DeleteMembershipParams object
// with the default values initialized.
func NewDeleteMembershipParams() *DeleteMembershipParams {
	var ()
	return &DeleteMembershipParams{

		timeout: cr.DefaultTimeout,
	}
}

// NewDeleteMembershipParamsWithTimeout creates a new DeleteMembershipParams object
// with the default values initialized, and the ability to set a timeout on a request
func NewDeleteMembershipParamsWithTimeout(timeout time.Duration) *DeleteMembershipParams {
	var ()
	return &DeleteMembershipParams{

		timeout: timeout,
	}
}

// NewDeleteMembershipParamsWithContext creates a new DeleteMembershipParams object
// with the default values initialized, and the ability to set a context for a request
func NewDeleteMembershipParamsWithContext(ctx context.Context) *DeleteMembershipParams {
	var ()
	return &DeleteMembershipParams{

		Context: ctx,
	}
}

// NewDeleteMembershipParamsWithHTTPClient creates a new DeleteMembershipParams object
// with the default values initialized, and the ability to set a custom HTTPClient for a request
func NewDeleteMembershipParamsWithHTTPClient(client *http.Client) *DeleteMembershipParams {
	var ()
	return &DeleteMembershipParams{
		HTTPClient: client,
	}
}

/*DeleteMembershipParams contains all the parameters to send to the API endpoint
for the delete membership operation typically these are written to a http.Request
*/
type DeleteMembershipParams struct {

	/*ID
	  Membership UUID

	*/
	ID strfmt.UUID

	timeout    time.Duration
	Context    context.Context
	HTTPClient *http.Client
}

// WithTimeout adds the timeout to the delete membership params
func (o *DeleteMembershipParams) WithTimeout(timeout time.Duration) *DeleteMembershipParams {
	o.SetTimeout(timeout)
	return o
}

// SetTimeout adds the timeout to the delete membership params
func (o *DeleteMembershipParams) SetTimeout(timeout time.Duration) {
	o.timeout = timeout
}

// WithContext adds the context to the delete membership params
func (o *DeleteMembershipParams) WithContext(ctx context.Context) *DeleteMembershipParams {
	o.SetContext(ctx)
	return o
}

// SetContext adds the context to the delete membership params
func (o *DeleteMembershipParams) SetContext(ctx context.Context) {
	o.Context = ctx
}

// WithHTTPClient adds the HTTPClient to the delete membership params
func (o *DeleteMembershipParams) WithHTTPClient(client *http.Client) *DeleteMembershipParams {
	o.SetHTTPClient(client)
	return o
}

// SetHTTPClient adds the HTTPClient to the delete membership params
func (o *DeleteMembershipParams) SetHTTPClient(client *http.Client) {
	o.HTTPClient = client
}

// WithID adds the id to the delete membership params
func (o *DeleteMembershipParams) WithID(id strfmt.UUID) *DeleteMembershipParams {
	o.SetID(id)
	return o
}

// SetID adds the id to the delete membership params
func (o *DeleteMembershipParams) SetID(id strfmt.UUID) {
	o.ID = id
}

// WriteToRequest writes these params to a swagger request
func (o *DeleteMembershipParams) WriteToRequest(r runtime.ClientRequest, reg strfmt.Registry) error {

	if err := r.SetTimeout(o.timeout); err != nil {
		return err
	}
	var res []error

	// path param id
	if err := r.SetPathParam("id", o.ID.String()); err != nil {
		return err
	}

	if len(res) > 0 {
		return errors.CompositeValidationError(res...)
	}
	return nil
}
